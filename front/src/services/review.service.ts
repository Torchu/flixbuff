import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError } from 'rxjs';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Review } from 'src/models/review';
import { instanceToPlain } from 'class-transformer';

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
}
