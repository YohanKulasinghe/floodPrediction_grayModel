import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgModule } from '@angular/core';
import {MatDialogModule} from '@angular/material/dialog';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ModelComponent } from './model/model.component';
import { NavbarComponent } from './navbar/navbar.component';
import { RouterModule } from '@angular/router';
import { ChartComponent } from './chart/chart.component';
import { ChartsModule } from 'ng2-charts';
import { AlertComponent } from './alert/alert.component';

@NgModule({
  entryComponents:[
    ChartComponent,
    AlertComponent
  ],
  declarations: [
    AppComponent,
    HomeComponent,
    ModelComponent,
    NavbarComponent,
    ChartComponent,
    AlertComponent
  ],
  imports: [
    ChartsModule,
    MatDialogModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      { path: '', component: HomeComponent },
      { path: 'model', component: ModelComponent },
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
