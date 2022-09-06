import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { User, UserList } from 'src/models/user';
import { catchError, map, throwError } from 'rxjs';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs/internal/Observable';
import { ReviewList } from 'src/models/review';
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

  /**
   * Gets the list of reviews of a user
   * @param {string} userId The ID of the user
   * @returns {Observable<ReviewList>} The list of reviews
   */
  public getReviews(userId: string): Observable<ReviewList> {
    return this.http.get<ReviewList>(`${this.path}/${userId}/reviews`).pipe(
      map((response) => plainToClass(ReviewList, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Gets a user
   * @param {string} userId The ID of the user
   * @returns {Observable<User>} The user
   */
  public get(userId: string): Observable<User> {
    return this.http.get<User>(`${this.path}/${userId}`).pipe(
      map((response) => plainToClass(User, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Follows a user
   * @param {string} userId The ID of the user
   * @returns {Observable<User>} The user
   */
  public follow(userId: string): Observable<User> {
    return this.http.put<User>(`${this.path}/follow/${userId}`, {}).pipe(
      map((response) => plainToClass(User, response)),
      catchError((err: HttpErrorResponse) => {
        let errorMessage: string;
        if (err.error && err.error.message) {
          errorMessage = 'Error: ' + err.error.message;
        } else if (err.error && err.error.msg) {
          errorMessage = 'Error: You must be logged in to perform this action';
        } else {
          errorMessage = 'Error: Something went wrong';
        }
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Unfollows a user
   * @param {string} userId The ID of the user
   * @returns {Observable<User>} The user
   */
  public unfollow(userId: string): Observable<User> {
    return this.http.put<User>(`${this.path}/unfollow/${userId}`, {}).pipe(
      map((response) => plainToClass(User, response)),
      catchError((err: HttpErrorResponse) => {
        let errorMessage: string;
        if (err.error && err.error.message) {
          errorMessage = 'Error: ' + err.error.message;
        } else if (err.error && err.error.msg) {
          errorMessage = 'Error: You must be logged in to perform this action';
        } else {
          errorMessage = 'Error: Something went wrong';
        }
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Gets the list of reviews of the users that the user follows
   * @returns {Observable<ReviewList>} The list of reviews
   */
  public getFriendsReviews(): Observable<ReviewList> {
    return this.http.get<ReviewList>(`${this.path}/friends/reviews`).pipe(
      map((response) => plainToClass(ReviewList, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }
}
