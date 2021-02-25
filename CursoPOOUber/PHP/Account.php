<?php
    class Account 
    {
        public $id; // Atributos
        public $name;
        public $document;
        public $email;
        public $password;
    }
    public function __construct ($name, $document){ // Metodo contructor
        $this->name = $name;
        $this->document = $document;
   }
?>