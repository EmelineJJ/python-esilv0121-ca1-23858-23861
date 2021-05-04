<!--Emeline JJ - 23858
Francoise RUCH - 23861 -->
<?php

$chemin = "Accounts/customers.txt";
$lignes = file($chemin);
echo"<table>";
foreach($lignes as $ligne){
    $ligne = explode("\t",$ligne)
    echo "<tr>";
    echo "<td>$ligne[0]</td>"
    echo "<td>$ligne[1]</td>"
    echo "<td>$ligne[2]</td>"
    echo "<td>$ligne[3]</td>"
    echo "<td>$ligne[4]</td>"
    echo " </tr>";
}
echo "</table>"
?>