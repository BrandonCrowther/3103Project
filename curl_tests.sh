curl -i -H "Content-Type: application/json" -X POST -d '{"username": "USERNAME HERE", "password": "PASSWORD HERE"}' -c cookie-jar -k https://info3103.cs.unb.ca:43005/signin
curl -i -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/signin
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"name":"Marvel"}'  -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"name":"DC"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"name":"CD"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"name":"DC"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/publisher
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"name":"Batman", "first_issue":"0", "last_issue":"52","start_year":"2011", "end_year":"2016", "publisher_id":"2"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/series
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"name":"New Avengers", "first_issue":"1", "last_issue":"17","start_year":"2015", "publisher_id":"1"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/series
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"name":"NewAvengers", "first_issue":"1", "last_issue":"17","start_year":"20000015",  "publisher_id":"1"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/series/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/series/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"name":"New Avengers", "first_issue":"1", "last_issue":"17","start_year":"2015",  "publisher_id":"1"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/series/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/series/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/series
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"first_name":"Scott", "last_name":"Snyder"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"first_name":"Al", "last_name":"Ewing"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"first_name":"Scott", "last_name":"Snayday"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"first_name":"Scott", "last_name":"Synder"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/writer
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"1","grade":"10.0", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"2", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"3", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"4", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"5","grade":7.8, "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"6","grade":9.5, "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"7", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"8", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"9","writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"10","writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"11", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"1","issue_number":"12","grade":"0.1", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"1", "writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"2", "writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"3","writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"4","writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"5","writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST --data '{"series_id":"2","issue_number":"6","writer_id":"2","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"series_id":"1","issue_number":"2","grade":"9.5", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X PUT --data '{"series_id":"1","issue_number":"2","grade":"10.0","image_url":"UPDATE SUCCESSFUL", "writer_id":"1","month":"08","year":"16"}' -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -X DELETE -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/1
curl -H "Accept: application/json" -H "Content-Type: application/json" -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic
curl -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/series/1
curl -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/publisher/1
curl -X GET -b cookie-jar -k https://info3103.cs.unb.ca:43005/comic/writer/1
curl -i -H "Content-Type: application/json" -X DELETE -b cookie-jar -k https://info3103.cs.unb.ca:43005/signin
