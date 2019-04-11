all : setup setup_routes 
	
setup:
	docker-compose up -d

setup_routes:
	#Delete default route (ROUTERS)
	docker exec -ti ospf_r1_1 ip -6 route del default
	docker exec -ti ospf_r2_1 ip -6 route del default
	docker exec -ti ospf_r3_1 ip -6 route del default
	docker exec -ti ospf_joker_1 ip -6 route del default
	docker exec -ti ospf_ww_1 ip -6 route del default
	docker exec -ti ospf_flash_1 ip -6 route del default
	docker exec -ti ospf_batman_1 ip -6 route del default
	docker exec -ti ospf_arrow_1 ip -6 route del default
	docker exec -ti ospf_superman_1 ip -6 route del default
	
	#Delete default route (HOST)
	docker exec -ti ospf_shazam_1 ip -6 route del default
	docker exec -ti ospf_marcian_1 ip -6 route del default
	docker exec -ti ospf_aquaman_1 ip -6 route del default

	#Setup IP Default (HOST)
	docker exec -ti ospf_shazam_1 ip -6 route add default via 2001::10
	docker exec -ti ospf_marcian_1 ip -6 route add default via 2009::10
	docker exec -ti ospf_aquaman_1 ip -6 route add default via 2012::10

clean:
	docker-compose down
	docker network prune

