<?php
require_once('Payment.php');
class Paypal extends Payment{
    public $email;
    public function __construct($id,$email){//Constructor
        parent::__construct($id);//Herencia
        this->$email = $email;
        
        }
    }
?>