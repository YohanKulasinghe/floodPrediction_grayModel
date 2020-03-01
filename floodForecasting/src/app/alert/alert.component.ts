import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.scss']
})
export class AlertComponent implements OnInit {

  alertMessage: any;
  imageURL: any;

  floodImage = "https://telisca.com/wp-content/themes/telisca-wp/assets/icons/Nav_Icons_166px_alert_applications.png"
  relaxImage = "https://images.all-free-download.com/images/graphicthumb/lifestyle_drawing_relaxed_people_park_icons_cartoon_design_6836190.jpg"

  constructor(@Inject(MAT_DIALOG_DATA) public data:any ) {
    this.alertMessage = this.data.alertMessage

    if(this.data.image == 1){
      this.imageURL = this.floodImage;
    }else{
      this.imageURL = this.relaxImage;
    }
   }

  ngOnInit() {
  }

}
