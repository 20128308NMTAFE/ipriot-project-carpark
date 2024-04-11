from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    car_park_moondalup = CarPark(location = "Moondalup", capacity = 100, log_file = "moondalup.txt")
    entry_sensor_moondalup = EntrySensor(id = 1, car_park = car_park_moondalup, is_active = True)
    exit_sensor_moondalup = ExitSensor(id = 2, car_park = car_park_moondalup, is_active = True)
    display_moondalup = Display(id = 1, car_park = car_park_moondalup, message = "Welcome to Moondalup", is_on = True)

    for i in range(10):
        entry_sensor_moondalup.detect_vehicle()

    for i in range(2):
        exit_sensor_moondalup.detect_vehicle()

if __name__ == "__main__":
    main()