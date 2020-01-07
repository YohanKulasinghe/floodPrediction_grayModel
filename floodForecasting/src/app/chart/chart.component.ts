import { Component, OnInit, Inject } from '@angular/core';
import { ChartDataSets, ChartOptions } from 'chart.js';
import { MAT_DIALOG_DATA } from '@angular/material';
import { Color, Label } from 'ng2-charts';

@Component({
  selector: 'app-chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent implements OnInit {
  l= [];
  a = []

  constructor(@Inject(MAT_DIALOG_DATA) public data:any) { 
    this.a = this.data.data
    for(let i = 1 ; i < this.a.length + 1 ; i++){
      this.l.push(i);
      } 
  }

  ngOnInit() {
       
  }

  lineChartData: ChartDataSets[] = [
    { data: this.data.data, label: 'Crude oil prices' },
  ];

  lineChartLabels: Label[] = this.l;

  lineChartOptions = {
    responsive: true,
  };

  lineChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,255,255,0)',
    },
  ];

  lineChartLegend = true;
  lineChartPlugins = [];
  lineChartType = 'line';
  

}
