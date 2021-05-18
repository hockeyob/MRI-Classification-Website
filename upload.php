<?php

if(isset($_FILES['file']['name'])){
   // file name
   $filename = $_FILES['file']['name'];

   // Location
   $location = 'uploads/uploaded_file.nii';

   // file extension
   $file_extension = pathinfo($location, PATHINFO_EXTENSION);
   $file_extension = strtolower($file_extension);

   // Valid extensions
   $valid_ext = array("nii");
   $valid_names = array("ADexample.nii","MCIexample.nii","CNexample.nii","mystery.nii");

   $response = 0;

   if(in_array($file_extension, $valid_ext)){
      if(in_array($filename,$valid_names)){
         $location = 'uploads/' . $filename;
         if(move_uploaded_file($_FILES['file']['tmp_name'],$location)){
            $response = 1;
         }

      } else {
         $location = 'uploads/uploaded_file.nii';
         if(move_uploaded_file($_FILES['file']['tmp_name'],$location)){
            $response = 1;
         }
      }
   }
   echo $response;
   exit;
}
?>