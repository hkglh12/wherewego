package com.kkk.wherewego;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {
        String MainTag = "";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        MainTag = "Main Act";

        final int locationPermission = ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION);
        final int PERMISSION_REQUEST_CODE = 100;
        String[] REQUIRED_PERMISSIONS = {Manifest.permission.ACCESS_FINE_LOCATION};
        final Context MainContext = getApplicationContext();
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(locationPermission != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, REQUIRED_PERMISSIONS, 100);
        }
        ImageButton near_me = (ImageButton)findViewById(R.id.Nearme);
        near_me.setOnClickListener((new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.e(MainTag, "near_me Button Clicked");
                Intent intent = new Intent(MainContext, NearmeActivity.class);
                intent.putExtra("message", "parameter");
                // 다른 activity에서 단일 인자값으로 넘길방법을 하나 찾아둠
                // reference : https://javannspring.tistory.com/145
                startActivity(intent);
            }
        }));

        ImageButton find_route = (ImageButton)findViewById(R.id.findroute);
        find_route.setOnClickListener((new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.e(MainTag, "find_route Button Clicked");
                Intent intent = new Intent(MainContext, routeActivity.class);
                intent.putExtra("message", "parameter");
                startActivity(intent);
            }
        }));

        ImageButton theme = (ImageButton)findViewById(R.id.theme);
        theme.setOnClickListener((new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.e(MainTag, "theme Button Clicked");
                Intent intent = new Intent(MainContext, themeActivity.class);
                intent.putExtra("message", "parameter");
                startActivity(intent);
            }
        }));

        ImageButton help = (ImageButton)findViewById(R.id.help);
        help.setOnClickListener((new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.e(MainTag, "help Button Clicked");
                Intent intent = new Intent(MainContext, themeActivity.class);
                intent.putExtra("message", "parameter");
                startActivity(intent);
            }
        }));

        ImageButton settings = (ImageButton)findViewById(R.id.settings);
        settings.setOnClickListener((new View.OnClickListener(){
            @Override
            public void onClick(View v){
                Log.e(MainTag, "settings Button Clicked");
                Intent intent = new Intent(MainContext, themeActivity.class);
                intent.putExtra("message", "parameter");
                startActivity(intent);
            }
        }));
    }
}
