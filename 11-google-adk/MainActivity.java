package com.example.studentassistant;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // step 1: find the button and the text on the screen
        Button askButton = findViewById(R.id.askButton);
        TextView resultText = findViewById(R.id.resultText);

        // step 2: when the button is clicked, show an answer
        askButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                resultText.setText("A linked list connects items using pointers.");
            }
        });
    }
}