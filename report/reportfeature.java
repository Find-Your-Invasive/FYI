/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.edu.morpheustest.report;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import javax.enterprise.context.RequestScoped;
import javax.inject.Named;

/**
 *
 * @author Ayaan
 */
@Named
@RequestScoped
public class reportfeature {
    
    private String address, city, state, zipcode;
    private String invasivename;
    
    public String getInvasivename() {
        return invasivename;
    }

    public void setInvasivename(String invasivename) {
        this.invasivename = invasivename;
    }
  
    public List<String> getInvasiveList2(String query){
        System.out.println(query);
        List<String> invasives = new ArrayList<>();
        invasives.add("HemlockWoollyAdelgid");
        invasives.add("EmeraldAshBorer");
        return invasives;
    }
    
    public String getAddress() {
        return address;
    }
    public void setAddress(String a) {
        this.address = a;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    
    public void reportsaver() throws IOException{
        //ArrayList<String> report = new ArrayList<>();
        String fulladdress = address + city + state + zipcode;
        //report.add(invasivename);
        //report.add(fulladdress);
        FileWriter csvWriter = new FileWriter("D:/Programming/reportedlocations.csv");
        csvWriter.append(String.join(",", invasivename + " "));
        csvWriter.append(String.join(",", fulladdress));
        csvWriter.flush();
        csvWriter.close();
        System.out.println("Done");
    }
}
