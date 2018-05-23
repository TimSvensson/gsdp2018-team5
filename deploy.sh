#!/usr/bin/bash


MYSQL_ROOT_PASSWORD=GSPDT15

function requirements {
	if [ "$(lsb_release -a | grep Distributor\ ID | awk '{print $3}')" == "Fedora" ]; then
		/usr/bin/dnf -y install python3 python3-pip python3-mysql mysql-server
	else
		echo "This Script Only Works on Fedora"
		exit
	fi
}

function setupMysqlService {
	systemctl enable mariadb
	systemctl start mariadb
}

function setupMysqlRootPassword {
	mysqladmin -uroot password $MYSQL_ROOT_PASSWORD
}

function setupMysqlDatabase {
	mysql -uroot -p$MYSQL_ROOT_PASSWORD < ./DB/DataBase.sql
	mysql -uroot -p$MYSQL_ROOT_PASSWORD automated_warehouse_management < ./DB/PopulateDataBase.sql
}

requirements
setupMysqlService
setupMysqlRootPassword
setupMysqlDatabase
