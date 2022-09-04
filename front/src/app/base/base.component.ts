import { AuthService } from 'src/services/auth.service';
import { Component } from '@angular/core';
import { LoginComponent } from '../login/login.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-base',
  templateUrl: './base.component.html',
  styleUrls: ['./base.component.scss']
})
export class BaseComponent {
  constructor(public dialog: MatDialog, private authService: AuthService) {}

  /**
   * Whether the user is logged in or not
   * @returns {boolean} Whether the user is logged in or not
   */
  isLogged(): boolean {
    return this.authService.loggedIn();
  }

  /**
   * Returns the user
   * @returns {string} The user data
   */
  getUser(): string {
    return this.authService.getUser();
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
