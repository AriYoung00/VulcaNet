'''
0.2 pressure (torr)
    760 is normal, make this the floor, anything less decreases risk of fire i.e. pressure - 760
    make pressure dependent on height
    The highest adjusted-to-sea level barometric pressure ever recorded on Earth (above 750 meters) was 1084.8 hPa (32.03
    inHg) measured in Tosontsengel, Mongolia on 19 December 2001. (wikipedia: temperature pressure altitude)
    Low pressure areas tend to have rain, so this justifies lowering risk of fire
0.1 altitude (meters)
    altitude form is 1/(1 + abs(altitude))
0.2 co2 (ppm)
    make 400 the floor, anything less decreases risk of fire, i.e. val - (400)
    make 1000 the cap
0.5 temperature (in celsius)
    100 is cap for temp, anything above contributes 0.5
1Pa = 0.00750062

fire likelihood is out of 100

2 °C per thousand feet up to 36,000 feet

A standard temperature lapse rate is when the temperature decreases at the rate of approximately 3.5 °F or 2 °C per
thousand feet up to 36,000 feet, which is approximately –65 °F or –55 °C. Above this point, the temperature is
considered constant up to 80,000 feet.
(https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak/media/06_phak_ch4.pdf)

have just likelihood prediction (and maybe later also send a notification if there is high probability of fire already)

terminal_lapse_height = 10972.8 # height at which lapse rate becomes zero
lapse_rate = 2 if altitude < terminal_lapse_height else 0

p_rel = p_stat * ((temp)/(temp + lapse_rate()))
'''

def calculate_risk(altitude, temperature, pressure, air_qual):
    '''Calculate risk of fire. Returns a float in the range of 0 and 1
    '''
    total = 0

    # calculate altitude contribution
    ALTITUDE_WEIGHT = 0.1
    # contribution decreases as altitude increases
    total += (1/(1 + abs(altitude))) * ALTITUDE_WEIGHT

    # print("contribution from altitude: {}".format(total))

    TEMPERATURE_WEIGHT = 0.5
    if (temperature < 20):
        total += 0
    elif (temperature > 40):
        total += TEMPERATURE_WEIGHT
    else:
        total += ((temperature - 20)/20) * TEMPERATURE_WEIGHT

    # print("contribution from altitude + temperature: {}".format(total))

    PRESSURE_WEIGHT = 0.2
    # possibly add another condition to make pressure contribution negative, since
    # low pressure often indicates higher potential for rain
    if (pressure < 760):
        total += 0
    elif (pressure > 800):
        total += PRESSURE_WEIGHT
    else:
        total += ((pressure - 760)/40) * PRESSURE_WEIGHT

    # print("contribution from altitude + temperature + pressure: {}".format(total))

    AIR_QUAL_WEIGHT = 0.2
    if (air_qual < 400):
        total += 0
    elif (air_qual > 1000):
        total += AIR_QUAL_WEIGHT
    else:
        total += ((air_qual - 400)/600) * AIR_QUAL_WEIGHT

    # print("contribution from altitude + temperature + pressure + air_qual: {}".format(total))

    return total if total > 0 else 0


def test():
    alt = 10000
    temp = 50
    press = 0
    air_qual = 0
    print(calculate_risk(alt, temp, press, air_qual))
    alt = 0
    temp = 0
    press = 0
    air_qual = 0
    print(calculate_risk(alt, temp, press, air_qual))
    alt = 10000
    temp = 0
    press = 800
    air_qual = 0
    print(calculate_risk(alt, temp, press, air_qual))
    alt = 10000
    temp = 0
    press = 0
    air_qual = 1000
    print(calculate_risk(alt, temp, press, air_qual))