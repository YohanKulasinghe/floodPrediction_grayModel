import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'
 

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  rainfallData: any;
  waterlevelData: any;

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  onClickRainfall(){
    this.http.get('http://localhost:5000/getrainfalldata').subscribe(res=>{
      this.rainfallData = res;
    }); 
  }

  onClickWaterlevel(){
    this.http.get('http://localhost:5000/getwaterleveldata').subscribe(res=>{
      this.waterlevelData = res;
    }); 
  }
}
