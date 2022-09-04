import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from 'src/services/auth.service';
import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { MatTabChangeEvent } from '@angular/material/tabs';
import { User } from 'src/models/user';
import { UserService } from 'src/services/user.service';
import { skip } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  public loginForm: FormGroup;
  public userForm: FormGroup;
  public activeTab = 0;

  constructor(
    fb: FormBuilder,
    public dialogRef: MatDialogRef<LoginComponent>,
    private authService: AuthService,
    private userService: UserService,
    private snackBar: MatSnackBar
  ) {
    this.loginForm = fb.group({
      email: ['', Validators.compose([Validators.required, Validators.email])],
      password: ['', Validators.required]
    });
    this.userForm = fb.group({
      username: ['', Validators.required],
      email: ['', Validators.compose([Validators.required, Validators.email])],
      password: ['', Validators.required]
    });
  }

  /**
   * Logs in the user
   */
  public logIn(): void {
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
   * Register the user
   */
  public signIn(): void {
    this.userService.create(this.userForm.value).subscribe((user: User) =>
      this.authService
        .login({ email: user.email, password: this.userForm.value.password })
        .pipe(skip(1)) // Initialization
        .subscribe((token: string) => {
          if (token !== '') {
            this.dialogRef.close(true);
          } else {
            this.snackBar.open('Login failed', '', { duration: 3000 });
          }
        })
    );
  }

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close(false);
  }

  /**
   * When the tab changes it
   */
  public tabChanged(event: MatTabChangeEvent): void {
    this.activeTab = event.index;
  }
}
