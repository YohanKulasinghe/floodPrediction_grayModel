import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatDialog } from '@angular/material'
import { ChartComponent } from '../chart/chart.component';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  rainfallData: any;
  waterlevelData: any;
  
  isGetRainfallData = false;
  isGetWaterLevelData = false;

  rainfallAccuData: any;
  waterlevelAccuData: any;

  rainFallHatValus: any;
  waterLevelHatValus: any;

  isGetRainfallHatValues = false;
  isGetWaterLevelHatValues = false;



  constructor(
    private http: HttpClient,
    private dialog: MatDialog) { }

  ngOnInit() {
  }

  /**
   * Get Row Data
   */
  getRainfallData() {
    this.isGetRainfallData = true;
    this.http.get('http://localhost:5000/getrainfalldata').subscribe(res => {
      this.rainfallData = res;
    });
  }

  getWaterlevelData() {
    this.isGetWaterLevelData = true;
    this.http.get('http://localhost:5000/getwaterleveldata').subscribe(res => {
      this.waterlevelData = res;
    });
  }

  /**
   * Get Accumilated Data
   */
  getAccuRainFallData() {
    this.isGetRainfallHatValues = true;
    this.http.post('http://localhost:5000/getAccumilatedData', { 'rowData': this.rainfallData }).subscribe(res => {
      this.rainfallAccuData = res;
    });
  }

  getAccuWaterLevelData() {
    this.isGetWaterLevelHatValues = true;
    this.http.get('http://localhost:5000/getAccumilatedData').subscribe(res => {
      this.waterlevelAccuData = res;
    });
  }

  /**
   * View Row Data
   */
  rainfallView() {
    this.dialog.open(ChartComponent, {data: {data: this.rainfallData}});
  }

  waterlevelView() {
    this.dialog.open(ChartComponent, {data: {data: this.waterlevelData}});
  }

  /**
   * View Accumilated Data
   */

  AccuRainfallView() {
    this.dialog.open(ChartComponent, {data: {data: this.rainfallAccuData}});
  }

  AccuWaterlevelView() {
    this.dialog.open(ChartComponent, {data: {data: this.waterlevelAccuData}});
  }

  /**
   * Get Z values
   */
  getRainFallHatValues(){
    this.http.post('http://localhost:5000/initializesModel',{ 'accuData': this.rainfallAccuData, 'rowData': this.rainfallData }).subscribe(res => {
      this.rainFallHatValus = res;
    });
  }

  getWaterLevelHatValues(){
    this.http.post('http://localhost:5000/initializesModel',{ 'accuData': this.waterlevelAccuData, 'rowData': this.waterlevelData }).subscribe(res => {
      this.waterLevelHatValus = res;
    });
  }

  
}
