package com.kkk.wherewego;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.TextView;
import android.widget.ToggleButton;

import java.util.List;

// LocationManager : reference : https://bitsoul.tistory.com/130
public class NearmeActivity extends AppCompatActivity {
    String NearTag = "";
    TextView now_location;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        // title바 제거
        // Reference : https://ghj1001020.tistory.com/9
        setContentView(R.layout.activity_nearme);
        NearTag = "Near Act";
        final Context NearContext = getApplicationContext();
        final TextView locmanager = (TextView)findViewById(R.id.LocationManager);
        now_location = (TextView)findViewById(R.id.NowLocation);
        final ToggleButton switcher = (ToggleButton)findViewById(R.id.toggle1);
        // 위치정보 수신 reference : https://bitsoul.tistory.com/131?category=623707
        final LocationManager lm = (LocationManager)getSystemService(Context.LOCATION_SERVICE);

        List<String> list = lm.getAllProviders();

        String str = "All Location Managers lists: \n";
        for(int i = 0; i<list.size(); i++)  {
            str += "Location Provied : " + list.get(i) + ", able? - "
                    + lm.isProviderEnabled(list.get(i)) + "\n";
        }
        locmanager.setText(str);

        switcher.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                try{
                    if(switcher.isChecked())    {
                        now_location.setText("Listening");
                        lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 100, 1, mLocationListener);
                        lm.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 100, 1, mLocationListener);
                    } else {
                        now_location.setText("Waiting for Action");
                        lm.removeUpdates(mLocationListener);
                    }
                }catch(SecurityException ex){

                }
            }
        });
    } // Oncreate Fin
   // Ref  :  https://bitsoul.tistory.com/131?category=623707
    private final LocationListener mLocationListener = new LocationListener(){
        public void onLocationChanged(Location location) {
            Log.e(NearTag, "Location changed, loc : " + location);
            double longitude = location.getLongitude();
            double latitude = location.getLatitude();
            double altitude = location.getAltitude();
            float accuracy = location.getAccuracy();
            String provider = location.getProvider();

            now_location.setText("위치정보 : " + provider + "\n위도 : " + longitude + "\n경도 : " + latitude
                    + "\n고도 : " + altitude + "\n정확도 : "  + accuracy);

        }
        public void onProviderDisabled(String provider){
            Log.e(NearTag, "on Provider disabled" + provider);
        }
        public void onProviderEnabled(String provider){
            Log.e(NearTag, "on Provider Enabled" + provider);
        }
        public void onStatusChanged(String provider, int status, Bundle extras) {
            Log.e(NearTag, "on status changed : Provider "
                    + provider + ", status:" + status  + ", Bundle:" + extras);
        }
    };
}
