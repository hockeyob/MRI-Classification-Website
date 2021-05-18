<?php 
$command = escapeshellcmd('python /var/www/html/python_scripts/fsl_segment.py');
$output = shell_exec($command);
echo $output;
?>
