import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { User, UserList } from 'src/models/user';
import { catchError, map, throwError } from 'rxjs';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs/internal/Observable';
import { plainToClass } from 'class-transformer';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  /**
   * Api path
   * @type {string}
   */
  private path = '/user';

  /**
   * Constructor
   * @param {HttpClient} http
   * @param {ApiService} apiService
   * @param {MatSnackBar} snackBar
   */
  constructor(private http: HttpClient, private apiService: ApiService, private snackBar: MatSnackBar) {
    this.path = this.apiService.getApiUrl() + this.path;
  }

  /**
   * Creates a new user
   * @param {User} user The user to create
   * @returns {Observable<User>} The created user
   */
  public create(user: User): Observable<User> {
    return this.http.post<User>(`${this.path}`, user).pipe(
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Gets the list of users
   * @param {query} query The query to filter the users
   * @returns {Observable<UserList>} The list of users
   */
  public list(query = ''): Observable<UserList> {
    return this.http.get<UserList>(`${this.path}`, { params: { query: query } }).pipe(
      map((response) => plainToClass(UserList, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }
}
