import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/services/auth.service';
import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { skip } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  public loginForm: FormGroup;

  constructor(
    fb: FormBuilder,
    public dialogRef: MatDialogRef<LoginComponent>,
    private authService: AuthService,
    private snackBar: MatSnackBar
  ) {
    this.loginForm = fb.group({
      email: ['', Validators.compose([Validators.required, Validators.email])],
      password: ['', Validators.required]
    });
  }

  /**
   * Logs in the user
   */
  public login(): void {
    this.authService
      .login(this.loginForm.value)
      .pipe(skip(1)) // Initialization
      .subscribe((token: string) => {
        if (token !== '') {
          this.dialogRef.close(true);
        } else {
          this.snackBar.open('Login failed', '', { duration: 3000 });
        }
      });
  }

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close(false);
  }
}
