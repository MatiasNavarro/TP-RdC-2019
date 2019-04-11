setup:
	docker-compose -p lab01 up -d

clean:
	docker-compose -p lab01 down

delete_routes:
	docker exec -ti lab01_b1_1 ip -6 route del default;
	docker exec -ti lab01_b2_1 ip -6 route del default;
	docker exec -ti lab01_r2_1 ip -6 route del default;
	docker exec -ti lab01_r1_1 ip -6 route del default;

