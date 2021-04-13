select * from app_rawfile where GPSfreq is NULL 

select count(*) from app_rawfile 

select * from app_rawfile where fileName ='GH023061'

select DISTINCT timeZone from app_rawfile

select * from app_rawfile where GPSfreq is not NULL and GMTtime is NULL 

select * from app_rawfile where municipality = '' and county != ''

select * from app_rawfile where country_int = '' and continent != ''