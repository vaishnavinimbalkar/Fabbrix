import pandas as pd

def calculate_discount_max(rating_value, margin_value, category_value, gender_value):
    """
    This function has all rules to create discount_max data. It creates training data for model.
    
    Args: 
    rating, margin, category, gender
    
    Returns:
    maximum discount
    
    """
    
    if rating_value < 3:
        discount = 30  # Low rating --> high discount
    elif margin_value > 30:
        discount = 40  # High margin --> higher discount
    else:
        discount = 5  # Default discount
    
    # Additional Discount based on category
    if category_value == 'Topwear':
        discount += 10
    
    # Additional Discount based on gender
    if gender_value == 'Girls':
        discount += 5
    
    return discount


def main(ip_product_table_path, op_save_product_table_path):

    data_df = pd.read_csv('product_table_without_discount.csv', sep = ';')
    
    rating = data_df['rating'].tolist()
    margin = data_df['margin'].tolist()
    category = data_df['category'].tolist()
    gender = data_df['gender'].tolist()
    
    discount_max_array = []

    for r, m, c, g in zip(rating, margin, category, gender):

        discount = calculate_discount_max(r,m,c,g)
        discount_max_array.append(discount)

    data_df['discount_max'] = (discount_max_array) 
    
    data_df.to_csv('product_table_with_discount.csv', index = None, sep = '\t')
    
    
if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser(description='Create training data for discount_max in product table')
    parser.add_argument('--ip_product_table_path', default = "data/product_table_without_discount.csv", type = str, help = '')
    parser.add_argument('--op_save_product_table_path', default = "data/product_table_with_discount.csv", type = str, help = '')
    args = parser.parse_args()
    
    main(args.ip_product_table_path, args.op_save_product_table_path)
    
    