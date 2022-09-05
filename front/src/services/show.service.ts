import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ShowList } from 'src/models/show';
import { plainToClass } from 'class-transformer';

@Injectable({
  providedIn: 'root'
})
export class ShowService {
  /**
   * Api path
   * @type {string}
   */
  private path = '/show';

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
   * Gets the list of shows
   * @param {string} query The query to search
   * @returns {Observable<ShowList>} The list of shows
   */
  public list(query: string): Observable<ShowList> {
    return this.http.get<ShowList>(`${this.path}`, { params: { query: query } }).pipe(
      map((response) => plainToClass(ShowList, response, { excludeExtraneousValues: true })),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }
}
