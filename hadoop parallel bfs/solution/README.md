student's name : 
student ID : 

how to run code :
                login to your server using any ssh and ftp client 

                upload the hadoop-streaming-3.1.4.jar , ass2.zip file and .pem file to your server using ftp

                change permission of the pem file  with the command 	chmod 400  32-cosc2637.pem

                now start the emr cluster with the bash script in the current location

                use command
                scp -i s3 32-cosc2637.pem  ass2.zip hadoop@s3 32.emr.cosc2637.route53.aws.rmit.edu.au:ass2.zip
                scp -i s3 32-cosc2637.pem  JAR.zip hadoop@s 232.emr.cosc2637.route53.aws.rmit.edu.au:JAR.zip

                use browser to see the hue with the link you got after creating the cluster . my link is
                http:// ue.cosc2637.route53.aws.rmit.edu.au:8888


                now login via ssh to the emr server using the command you got after creating the cluster 
                my command was 		ssh hadoop@s3 2.emr.cosc2637.route53.aws.rmit.edu.au -i s 2-cosc2637.pem

                unzip the zip file in the root path of the emr cluster


                change permission of the bash file using 	chmod +x run.sh 	command 

                now add the hadoop-streaming-3.1.4.jar file to the same directory 

                now go to the link  		http:// 2.hue.cosc2637.route53.aws.rmit.edu.au:8888/			and upload the graph.txt file to the hadoop folder of the website


                run below commands
                chmod 744 mapper.py
                chmod 744 reducer.py
                chmod 744 driver.py
                

                now comeback to the ssh client and run  	./run.sh 	in the directory where run.sh was extracted

                                