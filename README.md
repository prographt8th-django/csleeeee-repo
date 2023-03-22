# csleeeee-repo

## Subject
1. Django -(Task)-> Redis -> Celery -(Event)-> (Database or Result Store)
2. Django DRF Generics vs ViewSet (Source Code) and Serializer and Swagger
3. Django Error Log(Exception) and Middleware

### 1. Redis and Celery
* Redis란
  * Info
    * 채팅 고도화 with Caching
    * Compare Kafka vs RabbitMQ vs Redis
  * Redis는 데이터베이스의 하나인데 No-SQL이라고 말하는 비관계형 베이터 베이스에 속하는 데이터베이스이다.
  * No-SQL에도 여러 분류에 따라서 데이터베이스를 나눌 수 있지만 Redis는 그중에서도 Key-Value Type 데이터베이스에 속한다.
  * Key를 지정해서 Value를 저장하게되며 저장된 데이터를 사용할 때에는 지정된 Key를 통해서 저장된 데이터를 사용하게 된다.
  * 웹서버는 데이터가 존재하는지 Cache(Redis) 서버에 먼저 확인, 데이터가 있다면 DB 데이터를 조회하지 않고 Cache(Redis) 결과값을 Return

* Celery란
  * Info
    * 자정 마다 영수증 검증
    * Batch Job 으로 활용
    * 브로커
  * Python 동시성 프로그래밍에서 가장 많이 사용하는 방법 중 하나이며, 분산 메시지 전달을 기반으로 동작하는 비동기 작업 큐(Asynchronous Task/Job Queue)이다.
  * 이 API에 포함된 외부 연동이나 무거운 작업들은 Celery Task로 정의해서 Broker(RabbitMQ)와 Consumer(Celery Worker) 를 이용해 Async하게 처리함으로 써 사용자에게 가능한 빠른 응답 결과를 제공할 수 있을 것이다.
### 2. DRF Generics vs VietSet and Serializer and Swagger

### 3. Django Error Log and Middleware
