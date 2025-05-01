import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings("ignore")


def encode_array(input_array):
    # Define the category and gender mappings
    category_mapping = {'Apparel Set': 0, 'Bottomwear': 1, 'Dress': 2, 'Flip Flops': 3, 
                        'Sandal': 4, 'Shoes': 5, 'Socks': 6, 'Topwear': 7}
    
    gender_mapping = {'Boys': 0, 'Girls': 1, 'Men': 2, 'Women': 3}
    
    # Create a copy of the input array to store the encoded values
    encoded_array = []
    
    # Iterate over the input array and encode the values
    for item in input_array:
        if item in category_mapping:
            encoded_array.append(category_mapping[item])
        elif item in gender_mapping:
            encoded_array.append(gender_mapping[item])
        else:
            # If it's not in the mappings, assume it's a number and keep it as is
            encoded_array.append(item)
    
    return np.array(encoded_array)


def load_model(model_path = 'discount_prediction_model.pkl'):
    with open(model_path, 'rb') as file:
        discount_prediction_model = pickle.load(file)
    
    print("Model loaded successfully.")
    return discount_prediction_model


def run_model(model, encoded_input_array):
    
    encoded_input_array = encoded_input_array.reshape(1, -1)
    y_pred = discount_prediction_model.predict(encoded_input_array)
    discount_percent = int(y_pred[0])

    return discount_percent

    
def update_discount_DB(connection_params, discount_prediction_model, table_name = 'products'): 
 
    # Establish a connection
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()
    
        # Step 1: Fetch rows from the table
        #table_name = 'products'  # Replace with your table name
        cursor.execute(f"SELECT product_id, name, slug, price, description, image_url, discount_max, discount_price, rating, margin, category, gender FROM {table_name};")  # Replace column1, column2 as needed
        rows = cursor.fetchall()
    
        # Step 2: Process each row
        for row in rows:
            product_id = row[0]  
            price = row[3]
            discount_max = row[6]
            discount_price = row[7]
            rating = row[8]
            margin = row[9]
            category = row[10]
            gender = row[11]
            
            
            #print(row)
            # Perform the operation to compute discount_max and discount_price
            # 
            # Input sequence: [rating, margin, category, gender]
            sample_input = [rating, margin, category, gender]
            encoded_input = encode_array(sample_input)
            calc_discount = run_model(discount_prediction_model, encoded_input)

            discounted_price = price - price*(calc_discount/100)
            
    
            # Step 3: Update the row with the computed value
            cursor.execute(f"UPDATE {table_name} SET discount_max = %s WHERE product_id = %s;", (calc_discount, product_id))
            cursor.execute(f"UPDATE {table_name} SET discount_price = %s WHERE product_id = %s;", (discounted_price, product_id))

        print(f"{table_name} table updated successfully with", len(rows) ,"rows affected.")
        # Commit the transaction
        conn.commit()
    
    except Exception as e:
        print(f"Error: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":    
	
    print("\n\nFABBRIX --> This is product discount update stage.\n")
    
    # Define  connection parameters
    connection_params = {
       'dbname': 'fabbrix_db',
       'user': 'postgres',
       'password': 'vaish123',
       'host': 'localhost',  # or the IP address of your PostgreSQL server
       'port': '5432'        # default PostgreSQL port
     }


    discount_prediction_model = load_model(model_path = '../saved_models/discount_prediction_model.pkl')
    update_discount_DB(connection_params, discount_prediction_model, table_name = 'products')

