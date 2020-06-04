<?php
	if(isset($_GET['switchAlert'])){
                $value = shell_exec("/home/pi/hojung/switch_alert_php 2>&1");
                echo $value;
         }
	} else {
                echo "No Such Argument!!! by hojung.";
          }
?>

