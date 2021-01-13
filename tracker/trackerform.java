/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.edu.morpheustest.tracker;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
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
public class trackerform {
    private String address, city, state, zipcode;
    private String yearrange;
    private String invasivename;
    private String result;
    private String yearvalue;
    private int threatlevel;


    //invasivespecies
    public String getInvasivename() {
        return invasivename;
    }

    public void setInvasivename(String invasivename) {
        this.invasivename = invasivename;
    }
  
    public List<String> getInvasiveList(String query){
        System.out.println(query);
        List<String> invasives = new ArrayList<>();
        invasives.add("HemlockWoollyAdelgid");
        invasives.add("EmeraldAshBorer");
        return invasives;
    }
   
    //year
    public String getYearrange() {
        return yearrange;
    }

    public void setYearrange(String yearrange) {
        this.yearrange = yearrange;
    }
    
    public List<String> getYearList(String query){
        System.out.println(query);
        ArrayList<String> years = new ArrayList<>();
        years.add("2000-2020");
        years.add("2020-2040");
        years.add("2040-2060");
        years.add("2060-2080");
        years.add("2080-2100");
      
        return years;
    }
    
    //location
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
    
    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }
 
    public String modelSender(){
        try{
            String location = address + "," + city + "," + state + zipcode;
            location = location.replaceAll(" ", "");
            System.out.println(location);
            String u = "http://127.0.0.1:5000/?yearrange=" + yearrange + "&location=" + location + "&invasivename=" + invasivename;
            System.out.println(u);
            URL url = new URL(u);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("GET");
            if (conn.getResponseCode() != 200)
            {
                conn.disconnect();
                System.out.println("Error occurred");
//                return;
            }
            BufferedReader br = new BufferedReader( new InputStreamReader(conn.getInputStream()));
            result = br.readLine();
            System.out.println(result);
            conn.disconnect();            
                      
        } catch(MalformedURLException e){
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }
        return "trackerresults";
    }
}
