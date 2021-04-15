select * from app_rawfile where GPSfreq is NULL 

select count(*) from app_rawfile 

select count(*) from app_gpsdata

select * from app_rawfile where fileName ='GH023061'

select DISTINCT timeZone from app_rawfile

select * from app_rawfile where GPSfreq is not NULL and GMTtime is NULL 

select * from app_rawfile where municipality = '' and county != ''

select * from app_rawfile where country_int = '' and continent != ''

PRAGMA foreign_keys = ON

select count(*) from app_gpsdata 

delete from app_rawfile where id < 2075

update app_rawfile set trail = NULL where continent = 'America'

delete from app_rawfile 

delete from app_gpsdata 