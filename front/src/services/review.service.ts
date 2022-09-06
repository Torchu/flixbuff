import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';
import { Review, ReviewList } from 'src/models/review';
import { instanceToPlain, plainToClass } from 'class-transformer';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class ReviewService {
  /**
   * Api path
   * @type {string}
   */
  private path = '/review';

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
   * Creates a review
   * @param {Review} review The review to create
   * @returns {Observable<Review>} The created review
   */
  public create(review: Review): Observable<Review> {
    return this.http.post<Review>(`${this.path}`, instanceToPlain(review)).pipe(
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
   * Lists the reviews
   * @returns {Observable<ReviewList>} The list of reviews
   */
  public list(): Observable<ReviewList> {
    return this.http.get<ReviewList>(`${this.path}`).pipe(
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
