import { ApiService } from './api.service';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { CredentialsInterface } from 'src/interfaces/credentials.interface';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { LoginResponseInterface } from 'src/interfaces/login-response.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  /**
   * The Observable with access_token
   * @type {BehaviorSubject<String>}
   */
  private accessToken: BehaviorSubject<string>;

  /**
   * Api path
   * @type {string}
   */
  private path = '/auth';

  /**
   * Constructor
   * @param {HttpClient} http
   * @param {ApiService} apiService
   */
  constructor(private http: HttpClient, private apiService: ApiService) {
    this.accessToken = new BehaviorSubject<string>('');
    this.path = this.apiService.getApiUrl() + this.path;
  }

  /**
   * Logs the user in
   * @param {CredentialsInterface} credentials Credentials of the user
   */
  public login(credentials: CredentialsInterface): Observable<string> {
    this.http.post<LoginResponseInterface>(this.path, credentials).subscribe({
      next: (response: LoginResponseInterface) => {
        if (response.login_ok) {
          localStorage.setItem('access_token', response.access_token);
          localStorage.setItem('user', response.user.id); // TODO: Do I need this as an object? Maybe I need serialize.
          this.accessToken.next(response.access_token);
        } else {
          this.accessToken.next('');
        }
      },
      error: (_error) => {
        this.accessToken.next('');
      }
    });
    return this.accessToken.asObservable();
  }

  /**
   * Whether the user has a valid token or not
   * @returns {boolean}
   */
  public loggedIn(): boolean {
    return !!localStorage.getItem('userData');
  }

  /**
   * Removes the token from local storage and redirects the user to login page
   */
  public logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  }
}
