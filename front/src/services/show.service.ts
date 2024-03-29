import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';
import { Show, ShowList } from 'src/models/show';
import { ApiService } from './api.service';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
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
      map((response) => plainToClass(ShowList, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Gets a show
   * @param {number} id The show id
   * @returns {Observable<Show>} The show
   */
  public get(id: number): Observable<Show> {
    return this.http.get<Show>(`${this.path}/${id}`).pipe(
      map((response) => plainToClass(Show, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }

  /**
   * Gets the popular shows
   * @returns {Observable<ShowList>} The list of shows
   */
  public getPopular(): Observable<ShowList> {
    return this.http.get<ShowList>(`${this.path}/popular`).pipe(
      map((response) => plainToClass(ShowList, response)),
      catchError((err: HttpErrorResponse) => {
        const errorMessage =
          err.error && err.error.message ? 'Error: ' + err.error.message : 'Error: Something went wrong';
        this.snackBar.open(errorMessage, '', { duration: 3000 });
        return throwError(() => err);
      })
    );
  }
}
