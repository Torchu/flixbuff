import { Observable, map } from 'rxjs';
import { instanceToPlain, plainToClass, plainToInstance } from 'class-transformer';
import { ApiService } from './api.service';
import { BehaviorSubject } from 'rxjs/internal/BehaviorSubject';
import { CredentialsInterface } from 'src/interfaces/credentials.interface';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginResponse } from 'src/models/login-response';
import { User } from 'src/models/user';

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
   * @returns {Observable<string>} The access token
   */
  public login(credentials: CredentialsInterface): Observable<string> {
    this.http
      .post(`${this.path}/login`, credentials)
      .pipe(map((response) => plainToClass(LoginResponse, response), { excludeExtraneousValues: true }))
      .subscribe({
        next: (response: LoginResponse) => {
          if (response.loginOk) {
            localStorage.setItem('access_token', response.accessToken);
            localStorage.setItem('user', JSON.stringify(instanceToPlain(response.user)));
            this.accessToken.next(response.accessToken);
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
    return !!localStorage.getItem('user');
  }

  /**
   * Removes the token from local storage and redirects the user to login page
   */
  public logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
  }

  /**
   * Returns the user
   * @returns {User} The user data
   */
  public getUser(): User {
    return plainToInstance(User, JSON.parse(localStorage.getItem('user') || '{}') as unknown, {
      excludeExtraneousValues: true
    });
  }

  /**
   * Returns the access token
   * @returns {string} The access token
   */
  public getAccessToken(): string {
    return localStorage.getItem('access_token') || '';
  }

  /**
   * Sets the data for the current user
   * @param {User} user The user data
   */
  public setUser(user: User): void {
    localStorage.setItem('user', JSON.stringify(instanceToPlain(user)));
  }
}
