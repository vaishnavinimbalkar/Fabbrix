        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import LabelEncoder
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_absolute_error, mean_squared_error
        import pickle


        def label_encode(dataframe):
            
            category_mapping = {'Apparel Set': 0, 'Bottomwear': 1, 'Dress': 2, 'Flip Flops': 3, 
                            'Sandal': 4, 'Shoes': 5, 'Socks': 6, 'Topwear': 7}

            gender_mapping = {'Boys': 0, 'Girls': 1, 'Men': 2, 'Women': 3}
            
            # Apply mappings to respective columns
            dataframe['category'] = dataframe['category'].map(category_mapping)
            dataframe['gender'] = dataframe['gender'].map(gender_mapping)
            
            return dataframe 


        def create_data(csv_path = 'data/product_table_with_discount.csv'):

            df = pd.read_csv(csv_path, sep = '\t')
            encoded_df = label_encode(df)

            # Convert categorical features to numerical
            X = encoded_df.drop(['product_id', 'name', 'Slug', 'price', 'description', 'image_url', 'discount_max'], axis=1)
            y = encoded_df['discount_max']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            return X_train, X_test, y_train, y_test


        if __name__ == "__main__":

            X_train, X_test, y_train, y_test = create_data(csv_path = 'data/product_table_with_discount.csv')
            model = RandomForestRegressor(n_estimators=50, random_state=42)
            model.fit(X_train, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test)
            
            # Evaluate the model
            mae = mean_absolute_error(y_test, y_pred)
            print(f"Mean Absolute Error: {mae:.2f}")
            
            # Optional: Display feature importances
            importances = model.feature_importances_
            features = X_train.columns
            importances_df = pd.DataFrame({'Feature': features, 'Importance': importances})
            print("\nFeature Importances:")
            print(importances_df.sort_values(by='Importance', ascending=False))


            # Save the trained model to a file using pickle
            with open('../saved_models/discount_prediction_model_v2.pkl', 'wb') as file:
                pickle.dump(model, file)
                print("model saved successfully in saved_models directory: discount_prediction_model_v2.pkl")
                
                