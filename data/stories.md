## 01
* _greet
    - utter_greet
* _battery_search [car: mahindra xuv 500]
    - slot {"car": "mahindra xuv 500"}
    - utter_ask_user_info
* _user_detail [mobile:9810784182]
    - slot{"mobile":"9810784182"}
    - utter_ask_car_type
* _selection_car_type [car_type:petrol]
    - slot {"car_type":"petrol"}
    - action_provide_battery_options

## 02
* _battery_search [car: mahindra xuv 500]
    - slot {"car": "mahindra xuv 500"}
    - utter_ask_user_info
* _user_detail [mobile:9810784182]
    - slot {"mobile":"9810784182"}
    - utter_ask_car_type
* _selection_car_type [car_type:petrol]
    - slot {"car_type":"petrol"}
    - action_provide_battery_options

## 03
* _greet
    - utter_greet
* _user_detail [mobile:9810784182]
    - slot{"mobile":"9810784182"}
    - utter_ask_query
* _battery_search [car: mahindra xuv 500]
    - slot {"car": "mahindra xuv 500"}
    - utter_ask_car_type
* _selection_car_type [car_type:diesel]
    - slot {"car_type":"diesel"}
    - action_provide_battery_options


## 04
* _greet
    - utter_greet
* _battery_search [car: mahindra xuv 500, car_type: diesel]
    - slot {"car": "mahindra xuv 500", "car_type": "diesel"}
    - utter_ask_user_info
* _user_detail [mobile:9810784182]
    - slot {"mobile":"9810784182"}
    - action_provide_battery_options

## Generated Story -3831589686872434193
* _greet
    - utter_greet
* _battery_search[car=mahindra xuv 500,car_type=diesel]
    - slot{"car": "mahindra xuv 500"}
    - slot{"car_type": "diesel"}
    - utter_ask_user_info
* _user_detail[mobile=9763717974]
    - slot{"mobile": "9763717974"}
    - action_provide_battery_options

## Generated Story -7939417819316985009
* _battery_search[car=mahindra xuv]
    - slot{"car": "mahindra xuv"}
    - utter_ask_user_info
* _user_detail[mobile=9810784182]
    - slot{"mobile": "9810784182"}
    - utter_ask_car_type
* _selection_car_type[car_type=diesel]
    - slot{"car_type": "diesel"}
    - action_provide_battery_options

## Generated Story 351924252167947614
* _battery_search
    - utter_ask_car_info
* _car_details[car=mahindra scorpio,car_type=Diesel]
    - slot{"car": "mahindra scorpio"}
    - slot{"car_type": "Diesel"}
    - utter_ask_user_info
* _user_detail[mobile=9810784182]
    - slot{"mobile": "9810784182"}
    - action_provide_battery_options

## Generated Story 3590383094861546023
* _battery_search
    - utter_ask_car_info
* _car_details[car=hyundai i10]
    - slot{"car": "hyundai i10"}
    - utter_ask_car_type
* _car_details[car_type=PETROL]
    - slot{"car_type": "PETROL"}
    - utter_ask_user_info
* _user_detail[mobile=8888815255]
    - slot{"mobile": "8888815255"}
    - action_provide_battery_options

## Generated Story 7220021886014147514
* _greet
    - utter_greet
* _battery_search[car=mahindra xuv 500]
    - slot{"car": "mahindra xuv 500"}
    - utter_ask_user_info
* _user_detail[mobile=9810784182]
    - slot{"mobile": "9810784182"}
    - utter_ask_car_type
* _selection_car_type[car_type=diesel]
    - slot{"car_type": "diesel"}
    - action_provide_battery_options
