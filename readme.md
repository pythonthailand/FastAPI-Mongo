# fast api CRUD connect mongodb and run on docker

1.clone this repo

2.install docker

3.run command : `docker-compose up -d`

4.testing on api : http://localhost:8000
    - post http://localhost:8000/items
        body data
            {
                "name":"test",
                "description":"test"
            }
    - get all http://localhost:8000/items/
    - get by id http://localhost:8000/items/id
    - update http://localhost:8000/items/id 
        body data
            {
                "name":"test",
                "description":"test"
            }
    - delete http://localhost:8000/items/id

thankyou for reading pythonthailand.com

