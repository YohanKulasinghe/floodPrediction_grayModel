import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatDialog } from '@angular/material'
import { ChartComponent } from '../chart/chart.component';
import { connectableObservableDescriptor } from 'rxjs/internal/observable/ConnectableObservable';


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

  rainFallHatValusLabel: string;
  waterLevelHatValusLabel: string;
  kValue: any;

  predictedRainfall: any;
  predictedWaterLevel: any;

  getPrediction = false;

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
    this.http.post('http://localhost:5000/getAccumilatedData', { 'rowData': this.waterlevelData }).subscribe(res => {
      this.waterlevelAccuData = res;
    });
  }

  /**
   * View Row Data
   */
  rainfallView() {
    this.dialog.open(ChartComponent, {data: {data: this.rainfallData, label:'Rainfall Row Data'}});
  }

  waterlevelView() {
    this.dialog.open(ChartComponent, {data: {data: this.waterlevelData, label:'Waterlevel Row Data'}});
  }

  /**
   * View Accumilated Data
   */

  AccuRainfallView() {
    this.dialog.open(ChartComponent, {data: {data: this.rainfallAccuData, label:'Rainfall Data After AGO'}});
  }

  AccuWaterlevelView() {
    this.dialog.open(ChartComponent, {data: {data: this.waterlevelAccuData, label:'Waterlevel Data After AGO'}});
  }

  /**
   * Get Z values
   */
  getRainFallHatValues(){
    this.http.post('http://localhost:5000/initializesModel',{ 'accuData': this.rainfallAccuData, 'rowData': this.rainfallData }).subscribe(res => {
      this.rainFallHatValus = res;
      this.rainFallHatValusLabel = 'Success'
    });
  }

  getWaterLevelHatValues(){
    this.http.post('http://localhost:5000/initializesModel',{ 'accuData': this.waterlevelAccuData, 'rowData': this.waterlevelData }).subscribe(res => {
      this.waterLevelHatValus = res;
      this.waterLevelHatValusLabel = 'Success'
    });
  }

  /**
   * Get Forcasted values
   */

  onSubmit(){
    this.getRainFallForecastValue(this.kValue);
    this.getWaterLevelForecastValue(this.kValue);
  }

  
  getRainFallForecastValue(kValue){
    this.http.post('http://localhost:5000/rainfallprediction',{ 'rowData': this.rainfallData, 'hats':this.rainFallHatValus, 'k':kValue }).subscribe(res => {
      this.predictedRainfall = res;
      this.predictedRainfall = this.predictedRainfall.toFixed(3);
      this.getPrediction = true;
    });
  }

  getWaterLevelForecastValue(kValue){
    this.http.post('http://localhost:5000/waterlevelprediction',{ 'rowData': this.rainfallData, 'hats':this.waterLevelHatValus, 'k':kValue }).subscribe(res => {
      this.predictedWaterLevel = res;
      this.predictedWaterLevel = this.predictedWaterLevel.toFixed(3);
    });
  }


}
