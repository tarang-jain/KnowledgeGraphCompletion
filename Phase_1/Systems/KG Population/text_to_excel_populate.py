import pandas as pd
import os
import re
import sys
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')

data_frame = pd.read_excel('OntologyDataSchema.xlsx')
print(data_frame.shape)
column_names_list = data_frame.columns.values.tolist()

def extract_data_from_reports(report_path, report_count):
	report_text_file = open(report_path, 'r').readlines()
	data_frame.at[report_count, 'Accident'] = get_data(report_text_file, "Accident Number:")
	if(len(data_frame.at[report_count, 'Accident'])==0):
		return False
	data_frame.at[report_count, 'Aircraft'] = get_data(report_text_file, "Registration:")
	data_frame.at[report_count, 'AircraftManufacturer'] = get_data(report_text_file, "Aircraft Make:")
	data_frame.at[report_count, 'AircraftModel'] = get_data(report_text_file, "Model/Series:")
	data_frame.at[report_count, 'AircraftCategory'] = get_data(report_text_file, "Aircraft Category:")
	data_frame.at[report_count, 'AirworthinessCertificate'] = get_data(report_text_file, "Airworthiness Certificate:")
	data_frame.at[report_count, 'EngineManufacturer'] = get_data(report_text_file, "Engine Manufacturer:")
	data_frame.at[report_count, 'EngineModel'] = get_data(report_text_file, "Engine Model/Series:")
	data_frame.at[report_count, 'TypeOfAirspace'] = get_data(report_text_file, "Type of Airspace:", 1) #Faulty output
	data_frame.at[report_count, 'Pilot'] = 'Pilot_' + data_frame.at[report_count, 'Accident']
	data_frame.at[report_count, 'PilotCertificate'] = get_data(report_text_file, "Certificate:")
	data_frame.at[report_count, 'AirplaneRating'] = get_data(report_text_file, "Airplane Rating(s):")
	data_frame.at[report_count, 'Airport'] = get_data(report_text_file, "Airport:")
	data_frame.at[report_count, 'RunwaySurfaceType'] = get_data(report_text_file, "Runway Surface Type:")
	data_frame.at[report_count, 'InstrumentFlightRulesApproach'] = get_data(report_text_file, "IFR Approach:")
	data_frame.at[report_count, 'VisualFlightRulesApproach'] = get_data(report_text_file, "VFR Approach/Landing:", 1) #Faulty output,comes last
	data_frame.at[report_count, 'FederalAviationRegulation'] = get_data(report_text_file, "Flight Conducted Under:", 1) #Faulty output, comes last
	data_frame.at[report_count, 'Location'] = get_data(report_text_file, "Location:")
	data_frame.at[report_count, 'AircraftDamage'] = get_data(report_text_file, "Aircraft Damage:")
	data_frame.at[report_count, 'DefiningEvent'] = get_data(report_text_file, "Defining Event:")
	data_frame.at[report_count, 'AircraftIssue'] = get_data(report_text_file, "Aircraft issues", 1) #Faulty output
	data_frame.at[report_count, 'PersonnelIssue'] = get_data(report_text_file, "Personnel issues",1) #Faulty output
	data_frame.at[report_count, 'EnvironmentalIssue'] = get_data(report_text_file, "Environmental issues", 1) #Faulty output
	data_frame.at[report_count, 'DeparturePoint'] = get_data(report_text_file, "Departure Point:")
	data_frame.at[report_count, 'Destination'] = get_data(report_text_file, "Destination:")
	data_frame.at[report_count, 'YearOfManufacture'] = get_data(report_text_file, "Year of Manufacture:")
	data_frame.at[report_count, 'AmateurBulit'] = get_data(report_text_file, "Amateur Built:")
	data_frame.at[report_count, 'SerialNumber'] = get_data(report_text_file, "Serial Number:")
	data_frame.at[report_count, 'Seats'] = get_data(report_text_file, "Seats:")
	data_frame.at[report_count, 'DateTypeOfLastInspection'] = get_data(report_text_file, "Date/Type of Last Inspection:")
	data_frame.at[report_count, 'CertifiedMaxGrossWeight'] = get_data(report_text_file, "Certified Max Gross Wt.:")
	data_frame.at[report_count, 'TimeSinceLastInspection'] = get_data(report_text_file, "Time Since Last Inspection:")
	data_frame.at[report_count, 'AirframeTotalTime'] = get_data(report_text_file, "Airframe Total Time:")
	data_frame.at[report_count, 'ELT'] = get_data(report_text_file, "ELT:")
	data_frame.at[report_count, 'RegisteredOwner'] = get_data(report_text_file, "Registered Owner:")
	data_frame.at[report_count, 'RatedPower'] = get_data(report_text_file, "Rated Power:")
	data_frame.at[report_count, 'Operator'] = get_data(report_text_file, "Operator:", 1) #Faulty output, need to take one line only
	data_frame.at[report_count, 'OperatingCertificatesHeld'] = get_data(report_text_file, "Held:", 1) #Faulty output, comes at last
	data_frame.at[report_count, 'ConditionsAtAccidentSite'] = get_data(report_text_file, "Conditions at Accident Site:")
	data_frame.at[report_count, 'ConditionOfLight'] = get_data(report_text_file, "Condition of Light:")
	data_frame.at[report_count, 'ObservationFacilityElevation'] = get_data(report_text_file, "Observation Facility, Elevation:")
	data_frame.at[report_count, 'DistanceFromAccidentSite'] = get_data(report_text_file, "Distance from Accident Site:")
	data_frame.at[report_count, 'ObservationTime'] = get_data(report_text_file, "Observation Time:")
	data_frame.at[report_count, 'DirectionFromAccidentSite'] = get_data(report_text_file, "Direction from Accident Site:")
	data_frame.at[report_count, 'LowestCloudCondition'] = get_data(report_text_file, "Lowest Cloud Condition:", 1) #Faulty output
	data_frame.at[report_count, 'Visibility'] = get_data(report_text_file, "Visibility")
	data_frame.at[report_count, 'LowestCeiling'] = get_data(report_text_file, "Lowest Ceiling:")
	data_frame.at[report_count, 'VisibilityRVR'] = get_data(report_text_file, "Visibility (RVR):")
	data_frame.at[report_count, 'WindSpeedGusts'] = get_data(report_text_file, "Wind Speed/Gusts:", 1) #Faulty output
	data_frame.at[report_count, 'TurbulenceType'] = get_data(report_text_file, "Forecast/Actual:")
	data_frame.at[report_count, 'WindDirection'] = get_data(report_text_file, "Wind Direction:", 1) #Faulty output
	data_frame.at[report_count, 'TurbulenceSeverity'] = get_data(report_text_file, "Forecast/Actual:") #Faulty output, 2  line header
	data_frame.at[report_count, 'AltimeterSetting'] = get_data(report_text_file, "Altimeter Setting:")
	data_frame.at[report_count, 'TemperatureDewPoint'] = get_data(report_text_file, "Temperature/Dew Point:")
	data_frame.at[report_count, 'PrecipitationObscuration'] = get_data(report_text_file, "Precipitation and Obscuration:")
	data_frame.at[report_count, 'TypeOfFlightPlanFiled'] = get_data(report_text_file, "Type of Flight Plan Filed:")
	data_frame.at[report_count, 'TypeOfClearance'] = get_data(report_text_file, "Type of Clearance:")
	data_frame.at[report_count, 'DepartureTime'] = get_data(report_text_file, "Departure Time:")
	data_frame.at[report_count, 'AgeGender'] = get_data(report_text_file, "Age:")
	data_frame.at[report_count, 'SeatOccupied'] = get_data(report_text_file, "Seat Occupied:")
	data_frame.at[report_count, 'OtherAircraftRating'] = get_data(report_text_file, "Other Aircraft Rating(s):")
	data_frame.at[report_count, 'RestraintUsed'] = get_data(report_text_file, "Restraint Used:")
	data_frame.at[report_count, 'InstrumentRating'] = get_data(report_text_file, "Instrument Rating(s):")
	data_frame.at[report_count, 'SecondPilotPresent'] = get_data(report_text_file, "Second Pilot Present:")
	data_frame.at[report_count, 'InstructorRating'] = get_data(report_text_file, "Instructor Rating(s):")
	data_frame.at[report_count, 'ToxicologyPerformed'] = get_data(report_text_file, "Toxicology Performed:")
	data_frame.at[report_count, 'MedicalCertification'] = get_data(report_text_file, "Medical Certification:")
	data_frame.at[report_count, 'LastFAAMedicalExam'] = get_data(report_text_file, "Last FAA Medical Exam:")
	data_frame.at[report_count, 'OccupationalPilot'] = get_data(report_text_file, "Occupational Pilot:")
	data_frame.at[report_count, 'LastFlightReview'] = get_data(report_text_file, "Last Flight Review or Equivalent:")
	data_frame.at[report_count, 'AirportName'] = get_data(report_text_file, "Airport:")
	data_frame.at[report_count, 'AirportElevation'] = get_data(report_text_file, "Airport Elevation:")
	data_frame.at[report_count, 'RunwaySurfaceCondition'] = get_data(report_text_file, "Runway Surface Condition:")
	data_frame.at[report_count, 'RunwayUsed'] = get_data(report_text_file, "Runway Used:")
	data_frame.at[report_count, 'RunwayLengthWidth'] = get_data(report_text_file, "Runway Length/Width:")
	data_frame.at[report_count, 'LatitudeLongitude'] = get_data(report_text_file, "Latitude, Longitude:", 1) #Faulty output, comes last
	data_frame.at[report_count, 'TotalInjury'] = get_data(report_text_file, "Total Injuries:")
	data_frame.at[report_count, 'CrewInjury'] = get_data(report_text_file, "Crew Injuries:")
	data_frame.at[report_count, 'PassangerInjury'] = get_data(report_text_file, "Passenger Injuries:")
	data_frame.at[report_count, 'GroundInjury'] = get_data(report_text_file, "Ground Injuries:")
	data_frame.at[report_count, 'AircraftFire'] = get_data(report_text_file, "Aircraft Fire:")
	data_frame.at[report_count, 'AircraftExplosion'] = get_data(report_text_file, "Aircraft Explosion:")
	data_frame.at[report_count, 'DateTime'] = get_data(report_text_file, "Date & Time:")
	data_frame.at[report_count, 'LandingGearType'] = get_data(report_text_file, "Landing Gear Type:")
	data_frame.at[report_count, 'Engines'] = get_data(report_text_file, "Engines:")
	if(len(data_frame.at[report_count, 'Location'].split(', '))==2):
		data_frame.at[report_count, 'City'] = data_frame.at[report_count, 'Location'].split(', ')[0]
		data_frame.at[report_count, 'Country'] = data_frame.at[report_count, 'Location'].split(', ')[1]
	if(re.search('[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9],\s.*', data_frame.at[report_count, 'DateTypeOfLastInspection'])):
		data_frame.at[report_count, 'DateOfLastInspection'] = data_frame.at[report_count, 'DateTypeOfLastInspection'].split(', ')[0]
		data_frame.at[report_count, 'TypeOfLastInspection'] = data_frame.at[report_count, 'DateTypeOfLastInspection'].split(', ')[1]
	else:
		data_frame.at[report_count, 'TypeOfLastInspection'] = data_frame.at[report_count, 'DateTypeOfLastInspection']
	if("not installed" in data_frame.at[report_count, 'ELT'].lower()):
		data_frame.at[report_count, 'EmergencyLocatorTransmitterInstalled'] = 'No'
	elif("installed" in data_frame.at[report_count, 'ELT'].lower()):
		data_frame.at[report_count, 'EmergencyLocatorTransmitterInstalled'] = 'Yes'
	if("not activated" in data_frame.at[report_count, 'ELT'].lower()):
		data_frame.at[report_count, 'EmergencyLocatorTransmitterActivated'] = 'No'
	elif("activated" in data_frame.at[report_count, 'ELT'].lower()):
		data_frame.at[report_count, 'EmergencyLocatorTransmitterActivated'] = 'Yes'
	if(len(data_frame.at[report_count, 'ObservationFacilityElevation'].split(', '))==2):
		data_frame.at[report_count, 'ObservationFacility'] = data_frame.at[report_count, 'ObservationFacilityElevation'].split(', ')[0]
		data_frame.at[report_count, 'Elevation'] = data_frame.at[report_count, 'ObservationFacilityElevation'].split(', ')[1]
	if(" /" in data_frame.at[report_count, 'WindSpeedGusts']):
		data_frame.at[report_count, 'WindSpeed'] = data_frame.at[report_count, 'WindSpeedGusts'].split(' /')[0]
	if("/ " in data_frame.at[report_count, 'WindSpeedGusts']):
		data_frame.at[report_count, 'Gusts'] = data_frame.at[report_count, 'WindSpeedGusts'].split('/ ')[-1]
	if(" /" in data_frame.at[report_count, 'TurbulenceType']):
		data_frame.at[report_count, 'TurbulenceTypeForecast'] = data_frame.at[report_count, 'TurbulenceType'].split(' /')[0]
	if("/ " in data_frame.at[report_count, 'TurbulenceType']):
		data_frame.at[report_count, 'TurbulenceTypeActual'] = data_frame.at[report_count, 'TurbulenceType'].split('/ ')[-1]
	if(" /" in data_frame.at[report_count, 'TurbulenceSeverity']):
		data_frame.at[report_count, 'TurbulenceSeverityForecast'] = data_frame.at[report_count, 'TurbulenceSeverity'].split(' /')[0]
	if("/ " in data_frame.at[report_count, 'TurbulenceSeverity']):
		data_frame.at[report_count, 'TurbulenceSeverityActual'] = data_frame.at[report_count, 'TurbulenceSeverity'].split('/ ')[-1]
	if(" /" in data_frame.at[report_count, 'TemperatureDewPoint']):
		data_frame.at[report_count, 'Temperature'] = data_frame.at[report_count, 'TemperatureDewPoint'].split(' /')[0]
	if("/ " in data_frame.at[report_count, 'TemperatureDewPoint']):
		data_frame.at[report_count, 'DewPoint'] = data_frame.at[report_count, 'TemperatureDewPoint'].split('/ ')[-1]
	if("; " in data_frame.at[report_count, 'PrecipitationObscuration']):
		data_frame.at[report_count, 'Precipitation'] = str(data_frame.at[report_count, 'PrecipitationObscuration'].split('; ')[0]).split()[0] #Wrong output
		data_frame.at[report_count, 'Obscuration'] = str(data_frame.at[report_count, 'PrecipitationObscuration'].split('; ')[1]).split()[0] #wrong output
	if(" / " in data_frame.at[report_count, 'RunwayLengthWidth']):
		data_frame.at[report_count, 'RunwayLength'] = data_frame.at[report_count, 'RunwayLengthWidth'].split(' / ')[0]
		data_frame.at[report_count, 'RunwayWidth'] = data_frame.at[report_count, 'RunwayLengthWidth'].split(' / ')[1]
	if(", " in data_frame.at[report_count, 'LatitudeLongitude']):
		data_frame.at[report_count, 'Latitude'] = data_frame.at[report_count, 'LatitudeLongitude'].split(', ')[0]
		data_frame.at[report_count, 'Longitude'] = data_frame.at[report_count, 'LatitudeLongitude'].split(', ')[1]
	data_frame.at[report_count, 'AccidentNumber'] = 'AccidentNumber_' + data_frame.at[report_count, 'Accident']
	data_frame.at[report_count, 'Registration'] = 'Registration_' + data_frame.at[report_count, 'Aircraft']
	if(len(data_frame.at[report_count, 'CertifiedMaxGrossWeight'].split())>0 and str(data_frame.at[report_count, 'CertifiedMaxGrossWeight']).split()[0].isnumeric()):
		data_frame.at[report_count, 'CertifiedMaxGrossWeightFilter'] = data_frame.at[report_count, 'CertifiedMaxGrossWeight'].split()[0]
	if(len(data_frame.at[report_count, 'TimeSinceLastInspection'].split())>0 and str(data_frame.at[report_count, 'TimeSinceLastInspection']).split()[0].isnumeric()):
		data_frame.at[report_count, 'TimeSinceLastInspectionFilter'] = data_frame.at[report_count, 'TimeSinceLastInspection'].split()[0]
	if(', ' in data_frame.at[report_count, 'AgeGender'] and str(data_frame.at[report_count, 'AgeGender']).split(', ')[0].isnumeric()):
		data_frame.at[report_count, 'Age'] = data_frame.at[report_count, 'AgeGender'].split(', ')[0]
		data_frame.at[report_count, 'Gender'] = data_frame.at[report_count, 'AgeGender'].split(', ')[1]
	elif(str(data_frame.at[report_count, 'AgeGender']).isnumeric()):
		data_frame.at[report_count, 'Age'] = data_frame.at[report_count, 'AgeGender']
	if(', ' in data_frame.at[report_count, 'DateTime']):
		data_frame.at[report_count, 'Date'] = data_frame.at[report_count, 'DateTime'].split(', ')[0]
		data_frame.at[report_count, 'Time'] = data_frame.at[report_count, 'DateTime'].split(', ')[1]
	if(len(data_frame.at[report_count, 'RatedPower'].split())>0 and data_frame.at[report_count, 'RatedPower'].split()[0].isnumeric()):
		data_frame.at[report_count, 'RatedPowerFilter'] = data_frame.at[report_count, 'RatedPower'].split()[0]
	if(len(str(data_frame.at[report_count, 'Elevation']).split())>0 and str(data_frame.at[report_count, 'Elevation']).split()[0].isnumeric()):
		data_frame.at[report_count, 'ElevationFilter'] = str(data_frame.at[report_count, 'Elevation']).split()[0]
	if(len(str(data_frame.at[report_count, 'DistanceFromAccidentSite']).split())>0 and str(data_frame.at[report_count, 'DistanceFromAccidentSite']).split()[0].isnumeric()):
		data_frame.at[report_count, 'DistanceFromAccidentSiteFilter'] = str(data_frame.at[report_count, 'DistanceFromAccidentSite']).split()[0]
	data_frame.at[report_count, 'DirectionFromAccidentSiteFilter'] = "".join(e for e in str(data_frame.at[report_count, 'DirectionFromAccidentSite']) if e.isnumeric())
	if(len(str(data_frame.at[report_count, 'Visibility']).split())>0 and str(data_frame.at[report_count, 'Visibility']).split()[0].isnumeric()):
		data_frame.at[report_count, 'VisibilityFilter'] = str(data_frame.at[report_count, 'Visibility']).split()[0]
	if(len(str(data_frame.at[report_count, 'WindSpeed']).split())>0 and str(data_frame.at[report_count, 'WindSpeed']).split()[0].isnumeric()):
		data_frame.at[report_count, 'WindSpeedFilter'] = str(data_frame.at[report_count, 'WindSpeed']).split()[0]
	if(len(str(data_frame.at[report_count, 'Gusts']).split())>0 and str(data_frame.at[report_count, 'Gusts']).split()[0].isnumeric()):
		data_frame.at[report_count, 'GustsFilter'] = str(data_frame.at[report_count, 'Gusts']).split()[0]
	data_frame.at[report_count, 'WindDirectionFilter'] = "".join(e for e in str(data_frame.at[report_count, 'WindDirection']) if e.isnumeric())
	if(len(str(data_frame.at[report_count, 'AltimeterSetting']).split())>0):
		data_frame.at[report_count, 'AltimeterSettingFilter'] = float(str(data_frame.at[report_count, 'AltimeterSetting']).split()[0]) / 12
	data_frame.at[report_count, 'TemperatureFilter'] = "".join(e for e in str(data_frame.at[report_count, 'Temperature']) if e.isnumeric())
	data_frame.at[report_count, 'DewPointFilter'] = "".join(e for e in str(data_frame.at[report_count, 'DewPoint']) if e.isnumeric())
	if(len(str(data_frame.at[report_count, 'AirportElevation']).split())>0 and str(data_frame.at[report_count, 'AirportElevation']).split()[0].isnumeric()):
		data_frame.at[report_count, 'AirportElevationFilter'] = str(data_frame.at[report_count, 'AirportElevation']).split()[0]
	if(len(str(data_frame.at[report_count, 'RunwayLength']).split())>0 and str(data_frame.at[report_count, 'RunwayLength']).split()[0].isnumeric()):
		data_frame.at[report_count, 'RunwayLengthFilter'] = str(data_frame.at[report_count, 'RunwayLength']).split()[0]
	if(len(str(data_frame.at[report_count, 'RunwayWidth']).split())>0 and str(data_frame.at[report_count, 'RunwayWidth']).split()[0].isnumeric()):
		data_frame.at[report_count, 'RunwayWidthFilter'] = str(data_frame.at[report_count, 'RunwayWidth']).split()[0]
	if(len(str(data_frame.at[report_count, 'Longitude']).split())>0):
		data_frame.at[report_count, 'LongitudeFilter'] = str(data_frame.at[report_count, 'Longitude']).split()[0]
	else:
		data_frame.at[report_count, 'LongitudeFilter'] = ''
	if(len(str(data_frame.at[report_count, 'DateOfLastInspection']).split('/'))==3):
		data_frame.at[report_count, 'DateOfLastInspectionFilter'] = str(data_frame.at[report_count, 'DateOfLastInspection']).split('/')[2] + '-' + str(data_frame.at[report_count, 'DateOfLastInspection']).split('/')[0] + '-' + str(data_frame.at[report_count, 'DateOfLastInspection']).split('/')[1] + 'T00:00:00'
	if(len(str(data_frame.at[report_count, 'LastFAAMedicalExam']).split('/'))==3):
		data_frame.at[report_count, 'LastFAAMedicalExamFilter'] = str(data_frame.at[report_count, 'LastFAAMedicalExam']).split('/')[2] + '-' + str(data_frame.at[report_count, 'LastFAAMedicalExam']).split('/')[0] + '-' + str(data_frame.at[report_count, 'LastFAAMedicalExam']).split('/')[1] + 'T00:00:00'
	if(len(str(data_frame.at[report_count, 'LastFlightReview']).split('/'))==3):
		data_frame.at[report_count, 'LastFlightReviewFilter'] = str(data_frame.at[report_count, 'LastFlightReview']).split('/')[2] + '-' + str(data_frame.at[report_count, 'LastFlightReview']).split('/')[0] + '-' + str(data_frame.at[report_count, 'LastFlightReview']).split('/')[1] + 'T00:00:00'
	if(len(str(data_frame.at[report_count, 'Date']).split('/'))==3):
		data_frame.at[report_count, 'DateFilter'] = str(data_frame.at[report_count, 'Date']).split('/')[2] + '-' + str(data_frame.at[report_count, 'Date']).split('/')[0] + '-' + str(data_frame.at[report_count, 'Date']).split('/')[1]
	if(len(str(data_frame.at[report_count, 'ObservationTime']).split())==2 and str(data_frame.at[report_count, 'ObservationTime']).split()[0].isnumeric()):
		data_frame.at[report_count, 'ObservationTimeFilter'] = str(data_frame.at[report_count, 'DateFilter']) + 'T' + str(data_frame.at[report_count, 'ObservationTime']).split()[0][:2] + ':' + str(data_frame.at[report_count, 'ObservationTime']).split()[0][2:] + ':00'
		data_frame.at[report_count, 'ObservationTimeZone'] = str(data_frame.at[report_count, 'ObservationTime']).split()[1]
	if(len(str(data_frame.at[report_count, 'DepartureTime']).split())==2 and str(data_frame.at[report_count, 'DepartureTime']).split()[0].isnumeric()):
		data_frame.at[report_count, 'DepartureTimeFilter'] = str(data_frame.at[report_count, 'DateFilter']) + 'T' + str(data_frame.at[report_count, 'DepartureTime']).split()[0][:2] + ':' + str(data_frame.at[report_count, 'DepartureTime']).split()[0][2:] + ':00'
		data_frame.at[report_count, 'DepartureTimeZone'] = str(data_frame.at[report_count, 'DepartureTime']).split()[1]
	if(len(str(data_frame.at[report_count, 'Time']).split())==2 and str(data_frame.at[report_count, 'Time']).split()[0].isnumeric()):
		data_frame.at[report_count, 'TimeFilter'] = data_frame.at[report_count, 'DateFilter'] + 'T' + str(data_frame.at[report_count, 'Time']).split()[0][:2] + ':' + str(data_frame.at[report_count, 'Time']).split()[0][2:] + ':00'
		data_frame.at[report_count, 'TimeZone'] = str(data_frame.at[report_count, 'Time']).split()[1]
	
	#Feed units
	data_frame.at[report_count, 'CertifiedMaxGrossWeightUnit'] = "pound"
	data_frame.at[report_count, 'TimeSinceLastInspectionUnit'] = "hour"
	data_frame.at[report_count, 'RatedPowerUnit'] = "horsepower (boiler)"
	data_frame.at[report_count, 'ElevationUnit'] = "foot"
	data_frame.at[report_count, 'DistanceFromAccidentSiteUnit'] = "nautical mile"
	data_frame.at[report_count, 'DirectionFromAccidentSiteUnit'] = "degree [unit of angle]"
	data_frame.at[report_count, 'VisibilityUnit'] = "mile (statute mile)"
	data_frame.at[report_count, 'WindSpeedUnit'] = "knot"
	data_frame.at[report_count, 'GustsUnit'] = "knot"
	data_frame.at[report_count, 'WindDirectionUnit'] = "degree [unit of angle]"
	data_frame.at[report_count, 'AltimeterSettingUnit'] = "foot of mercury"
	data_frame.at[report_count, 'TemperatureUnit'] = "degree Celsius"
	data_frame.at[report_count, 'DewPointUnit'] = "degree Celsius"
	data_frame.at[report_count, 'AgeUnit'] = "year"
	data_frame.at[report_count, 'AirportElevationUnit'] = "foot"
	data_frame.at[report_count, 'RunwayLengthUnit'] = "foot"
	data_frame.at[report_count, 'RunwayWidthUnit'] = "foot"
	data_frame.at[report_count, 'LatitudeUnit'] = "degree [unit of angle]"
	data_frame.at[report_count, 'LongitudeUnit'] = "degree [unit of angle]"
	# data_frame.at[report_count, ''] = ""
	# data_frame.at[report_count, ''] = ""
	# data_frame.at[report_count, ''] = ""
	# data_frame.at[report_count, ''] = ""
	# data_frame.at[report_count, ''] = ""
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	# data_frame.at[report_count, ''] = get_data(report_text_file, "")
	return True

def get_data(report_text_file, data, line_count=50):
	result = ''
	i = 0 
	found_index = -1
	found = False
	while(i<len(report_text_file)):
		if(report_text_file[i].strip()==data):
			found_index = i + 1
			found = True
			break 
		i = i + 1
	if(not found):
		return "" #Not Found
	i = found_index
	j = 0
	while(i<len(report_text_file) and j<line_count):
		if(report_text_file[i].strip().endswith(':')):
			break
		result = result + ' ' + report_text_file[i].strip()
		i = i + 1
		j = j + 1
	return result.strip()

start_year = input('Enter start year: ')
end_year = input('Enter end year: ')
report_count = 0
# source_folder = 'SampleTexts'
source_folder = 'Texts'
for i in range(int(start_year), int(end_year) + 1):
	for j in range(1, 13):
		reports = os.listdir(source_folder + '/' + str(i) + '/' + str(j))
		reports.sort()
		for report in reports:
			report_path = source_folder + '/' + str(i) + '/' + str(j) + '/' + str(report)
			data_frame.at[report_count, 'File'] = str(report)
			if(extract_data_from_reports(report_path, report_count)):
				print('Extracted information from ' + str(report))
				report_count = report_count + 1
		print('####Extracted information from month ' + str(j) + ' of year ' + str(i))
	print('****Extracted information from ' + str(i) + ' year')

rows = data_frame.shape[0]
columns = data_frame.shape[1]
for r in range(rows):
	for c in range(columns):
		if(pd.isnull(data_frame.iat[r, c]) or data_frame.iat[r, c]==''):
			data_frame.iat[r, c] = '___Unknown___' + column_names_list[c]
		if(data_frame.iat[r, c] == '___Unknown___YearOfManufacture'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___AmateurBulit'):
			data_frame.iat[r, c] = 0
		if(data_frame.iat[r, c] == '___Unknown___Seats'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___DateOfLastInspectionFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		if(data_frame.iat[r, c] == '___Unknown___CertifiedMaxGrossWeightFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___TimeSinceLastInspectionFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___RatedPowerFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___ElevationFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___DistanceFromAccidentSiteFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___ObservationTimeFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		if(data_frame.iat[r, c] == '___Unknown___DirectionFromAccidentSiteFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___VisibilityFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___WindSpeedFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___GustsFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___WindDirectionFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___AltimeterSettingFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___TemperatureFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___DewPointFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___DepartureTimeFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		if(data_frame.iat[r, c] == '___Unknown___Age'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___LastFAAMedicalExamFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		if(data_frame.iat[r, c] == '___Unknown___LastFlightReviewFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		if(data_frame.iat[r, c] == '___Unknown___AirportElevationFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___RunwayUsed'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___RunwayLengthFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___RunwayWidthFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___Latitude'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___LongitudeFilter'):
			data_frame.iat[r, c] = 1000
		if(data_frame.iat[r, c] == '___Unknown___TimeFilter'):
			data_frame.iat[r, c] = "1000:01:01T00:00:00"
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =
		# if(data_frame.iat[r, c] == '___Unknown___'):
		# 	data_frame.iat[r, c] =


data_frame.to_excel('OntologyData.xlsx')
# print('*********************************')
