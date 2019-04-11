setup:
	docker-compose -p lab02 up -d

clean:
	docker-compose -p lab02 down

delete_routes:
	docker exec -ti lab02_b1_1 ip -6 route del default;
	docker exec -ti lab02_b2_1 ip -6 route del default;
	docker exec -ti lab02_r2_1 ip -6 route del default;
	docker exec -ti lab02_r1_1 ip -6 route del default;
	docker exec -ti lab02_mail_client_1 ip -6 route del default via 2001:aaaa:1111::1;
	docker exec -ti lab02_mail_server_1 ip -6 route del default via 2001:bbbb:2222::1;
	docker exec -ti lab02_mail_client_1 ip -6 route add default via 2001:aaaa:1111::10;
	docker exec -ti lab02_mail_server_1 ip -6 route add default via 2001:bbbb:2222::10;

check_connectivity:
	docker exec -ti lab02_mail_client_1 ping6 -c 3 2001:bbbb:2222::11;
	docker exec -ti lab02_mail_server_1 ping6 -c 3 2001:aaaa:1111::11;

send_mail:
	docker exec -ti lab02_mail_client_1 swaks --to matt@redes2019.org --server [2001:bbbb:2222::11]:1025 --body "Hello Matt! Are you awake ?" --header "Subject: Redes 2019"


