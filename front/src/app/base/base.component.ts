import { Component, OnInit } from '@angular/core';
import { LoginComponent } from '../login/login.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-base',
  templateUrl: './base.component.html',
  styleUrls: ['./base.component.scss']
})
export class BaseComponent implements OnInit {
  loggedIn = false;

  constructor(public dialog: MatDialog) {}

  ngOnInit(): void {
    // TODO: check if user is logged in looking at the session storage
    console.log('Iniciando Base');
  }

  log(): void {
    const dialogRef = this.dialog.open(LoginComponent, {
      width: '250px',
      height: '35%',
      panelClass: 'custom-dialog'
    });

    dialogRef.afterClosed().subscribe((result: boolean) => {
      if (result) {
        // this.loggedIn = true;
      } else {
        console.log('The dialog was closed');
      }
    });
  }
}
