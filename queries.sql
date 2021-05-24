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

select * from app_gpsdata where rawfileKey_id = 7212

delete from app_gpsdata where rawfileKey_id = 7211

delete from app_rawfile where id > 7077

select * from app_rawfile where name like '%0007%' 

update app_rawfile set view = 'front' where view is NULL

select id, name, fileFullName, vidLength, camFirmware, firstGoodGPSLat,  tagLocationLat, municipality, trail, view, gpsFreq from app_rawfile where id > 7025 and firstGoodGPSLat is NULL 

select *, (1619710535707000 - TS) from app_gpsdata where ABS((1619710535707000 - TS)) < 55000

select * from app_gpsdata where rawfileKey_id = 8898

delete from app_gpsdata where rawfileKey_id not in (select id from app_rawfile)

delete from app_rawfile_logger where rawfileKey_id not in (select id from app_rawfile)

select * from app_rawfile_logger where textlog like "%error%"

select * from app_rawfile_logger where textlog like ("%" || CHAR(10) || "%")

select * from app_rawfile where gpsfreq < 17 and id > 9240 and id not in (select rawfilekey_id from app_rawfile_logger where textlog like ("%" || CHAR(10) || "%"))



vacuum

delete from app_rawfile 

delete from app_gpsdata 

delete from app_rawfile_logger 
