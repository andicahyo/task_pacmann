import pandas as pd
import numpy as np

def feature_engineering():
    # ubah nama kolom
    cars_data.rename(columns={"dateCreated": "ad_created",
                             "dateCrawled": "date_crawled",
                             "fuelType": "fuel_type",
                             "lastSeen": "last_seen",
                             "monthOfRegistration": "registration_month",
                             "notRepairedDamage": "unrepaired_damage",
                             "nrOfPictures": "num_of_pictures",
                             "offerType": "offer_type",
                             "postalCode": "postal_code",
                             "powerPS": "power_ps",
                             "vehicleType": "vehicle_type",
                             "yearOfRegistration": "registration_year"}, inplace = True)
    
    # ubah tipe data colom menjadi datetime64
    col_date = ['ad_created', 'date_crawled', 'last_seen']

    for i in col_date:
        cars_data[i] = pd.to_datetime(cars_data[i])
    
    # menyeragamkan format penulisan nilai pada kolom tersebut sebelum di konversi
    cars_data['price'] = cars_data['price'].str.replace('$', '')
    cars_data['odometer'] = cars_data['odometer'].str.replace('km', '')

    cars_data['price'] = cars_data['price'].str.replace(',', '')
    cars_data['odometer'] = cars_data['odometer'].str.replace(',', '')
    
    # ubah tipe data dari object to int64
    col = ['price', 'odometer']

    for i in col:
        cars_data[i] = cars_data[i].astype('int64')
    
    # dari data dapat disimpulkan bahwa kolom:
    # offer_type dan kollom seller dan 
    # memiliki perbandingan data unik terlalu besar maka kita drop saja 

    cars_data = cars_data.drop(columns= ['offer_type', 'seller'], axis=1)
    
    # dari kolom numerik diatas kita bisa tau untuk data nol (0)
    # ada pada kolom num_of_picture

    cars_data = cars_data.drop(columns=['num_of_pictures'], axis=1)
    
    # Drop kolom yang informasinya unik disetiap baris datanya ("name")
    # dan kolom yang memiliki banyak kategori namun tidak balance("postal_code")

    cars_data = cars_data.drop(['name', 'postal_code'], axis=1)
    
    #ambil kolom price berkisar antara 500-40000 code by andi-8K6R

    cars_data= cars_data[(cars_data['price'] >=500) & (cars_data['price'] <= 40000)]
    
    # mengisi NaN data pada categorical dengan mode-nya

    nan_val = ['vehicle_type', 'gearbox', 'model', 'fuel_type', 'unrepaired_damage']

    for i in nan_val:
        cars_data[i] = cars_data[i].fillna(cars_data[i].mode()[0])
    
    
    return cars_data.info()