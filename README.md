# JWT SECRET
	a simple python script to brute force JSON WEB TOCKEN (JWT) secret using a dictionary 

# usage 
	./jwt_secret_brute.py -t <JWT> -a <hashing algorithm> -w <word list>	

# install 
	pip/pip3 install -r requirements.txt 

#example 
	python jwt_secret_brute.py -a HS256 -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcImFkbWluXCIsXCJyb2xlXCI6XCJhZG1pblwifSJ9.Gyjq_Oo2oiv77APuu5r2icnThEfKFnGHZRhG_3vQ_i4 -w /usr/share/wordlists/rockyou.txt	

	crunch 6 6 -t ran@@% | python jwt_secret_brute.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoie1widXNlcm5hbWVcIjpcImFkbWluXCIsXCJyb2xlXCI6XCJhZG1pblwifSJ9.Gyjq_Oo2oiv77APuu5r2icnThEfKFnGHZRhG_3vQ_i4 
