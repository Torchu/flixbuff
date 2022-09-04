import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  public loginForm: FormGroup;

  constructor(fb: FormBuilder, public dialogRef: MatDialogRef<LoginComponent>) {
    this.loginForm = fb.group({
      email: ['', Validators.compose([Validators.required, Validators.email])],
      password: ['', Validators.required]
    });
  }

  /**
   * Logs in the user
   */
  public login(): void {
    console.log(this.loginForm.value);
    this.dialogRef.close(true);
  }

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close(false);
  }
}
