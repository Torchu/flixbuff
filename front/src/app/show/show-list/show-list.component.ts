import { Component, OnInit } from '@angular/core';
import { debounceTime, switchMap } from 'rxjs';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { Show } from '../../../models/show';
import { ShowService } from 'src/services/show.service';

@Component({
  selector: 'app-show-list',
  templateUrl: './show-list.component.html',
  styleUrls: ['./show-list.component.scss']
})
export class ShowListComponent implements OnInit {
  searchBar: FormControl;
  showList: Array<Show> = [];

  constructor(private showService: ShowService, private router: Router) {
    this.searchBar = new FormControl('');
  }

  ngOnInit(): void {
    this.searchBar.valueChanges
      .pipe(
        debounceTime(500),
        switchMap((value: string) => this.showService.list(value))
      )
      .subscribe((shows) => {
        this.showList = shows.items;
      });
  }

  /**
   * Open the show details page
   * @param showId The show id
   */
  openDetails(showId: number): void {
    this.router.navigate(['show', showId]);
  }
}
