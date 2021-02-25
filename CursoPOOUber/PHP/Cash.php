<?php
require_once('Payment.php');
class Cash extends Payment{
    
    public function __construct($id){//Constrcutor
        parent::__construct($id);//Herencia

        }
    }
?>