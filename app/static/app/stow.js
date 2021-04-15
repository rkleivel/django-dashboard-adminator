$( document ).ready(function() {
    console.log( "ready!" );
    mydata.forEach(setMarker);
    reddata.forEach(setRedMarker);
    greendata.forEach(setGreenMarker);
    traildata.forEach(setTrailMarkers);
});

var mymap = L.map('mapid').setView([60.53, 5.14], 13);
    
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicmtsZWl2ZWwiLCJhIjoiY2ttbjdtNzhkMGV1cDJucGVkbWptZW40ciJ9.wy0hOi5vNPZKbembRjqI0g'
}).addTo(mymap);

//var marker1 = L.marker([60.53, 5.14]).addTo(mymap);
//var marker2 = L.marker([60.54, 5.15]).addTo(mymap);
const mydata = JSON.parse(document.getElementById('mydata').textContent);
const reddata = JSON.parse(document.getElementById('reddata').textContent);
const greendata = JSON.parse(document.getElementById('greendata').textContent);
const traildata = JSON.parse(document.getElementById('traildata').textContent);
//var pinStart = Array()
//var pinEnd = Array()
var pinLocation = Array()
var redCircle = Array()
var greenCircle = Array()
var trailCircle = Array()
function setMarker(item, index) {
    //pin[index] = L.marker([item.lat, item.lon]).addTo(mymap).bindPopup(item.file_name);
    pinLocation[index] = L.circle([item.firstGoodGPSLat, item.firstGoodGPSLon], {color: 'blue', radius: 25})
        .addTo(mymap)
        .bindTooltip(item.fileName + "<br>" + item.vidRecNumSeqNum +  "<br>" + item.mtimeStr + "<br>"  + item.localTimeStr + "<br>" + item.vidLengthStr)
        .bindPopup('mpv "' + item.fullPath + '"');
    //pinLocation[index] = L.marker([item.tagLocationLat, item.tagLocationLon]).addTo(mymap).bindPopup(item.fileName + "<br>" + item.localTimeStr);
    //pinEnd[index] = L.circle([item.lastGoodGPSLat, item.lastGoodGPSLon], {color: 'red', radius: 15}).addTo(mymap).bindPopup(item.name);
    //pin2[index] = L.circle([JSON.parse(item["tagLocation"])["lat"], JSON.parse(item["tagLocation"])["lon"]], {color: 'blue', radius: 20}).addTo(mymap).bindPopup(item.file_name);
}
function setRedMarker(item, index) {
    redCircle[index] = L.circle([item.tagLocationLat, item.tagLocationLon], {color: 'red', radius: 25})
        .addTo(mymap)
        .bindTooltip(item.fileName + "<br>" + item.vidRecNumSeqNum +  "<br>" + item.mtimeStr + "<br>" + item.localTimeStr + "<br>" + item.vidLengthStr)
        .bindPopup('mpv "' + item.fullPath + '"');
}
function setGreenMarker(item, index) {
    greenCircle[index] = L.circle([item.firstGoodGPSLat, item.firstGoodGPSLon], {color: 'green', radius: 25})
        .addTo(mymap)
        .bindTooltip(item.fileName + "<br>" + item.vidRecNumSeqNum +  "<br>" + item.mtimeStr + "<br>" + item.localTimeStr + "<br>" + item.vidLengthStr)
        .bindPopup('mpv "' + item.fullPath + '"');
}
function setTrailMarker(item, index) {
    trailCircle[index] = L.circle([item.Latitude, item.Longitude], {color: 'purple', radius: 10})
        .addTo(mymap);
}
function setTrailMarkers(item, index) {
    item.trail.forEach(setTrailMarker);
}


//var marker3 = L.marker([mydata.lat, mydata.lon]).addTo(mymap).bindPopup("GH010345");