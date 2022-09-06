import { Component, OnInit } from '@angular/core';
import { Review, ReviewList } from 'src/models/review';
import { Show, ShowList } from 'src/models/show';
import { ReviewService } from 'src/services/review.service';
import { Router } from '@angular/router';
import { ShowService } from 'src/services/show.service';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.scss']
})
export class FeedComponent implements OnInit {
  popularShowList: Array<Show> = [];
  latestReviewList: Array<Review> = [];
  popularCurrentPage = 0;
  latestCurrentPage = 0;
  latestLastPage: number;

  constructor(private router: Router, private showService: ShowService, private reviewService: ReviewService) {}

  ngOnInit(): void {
    this.showService.getPopular().subscribe((shows: ShowList) => {
      this.popularShowList = shows.items;
    });
    this.reviewService.list().subscribe((reviews: ReviewList) => {
      this.latestReviewList = reviews.items;
      this.latestLastPage = Math.ceil(this.latestReviewList.length / 4) - 1;
    });
  }

  /**
   * Open the show details page
   * @param showId The show id
   */
  openDetails(showId: number): void {
    this.router.navigate(['shows', showId]);
  }

  /**
   * Gets the page of the shows list
   * @param page The page
   * @returns {Array<Show>} The page
   */
  getPopularPaginated(page: number): Array<Show> {
    const pageSize = 5;
    return this.popularShowList.slice(page * pageSize, (page + 1) * pageSize);
  }

  /**
   * Gets the page of the latest reviews list
   * @param page The page
   * @returns {Array<Review>} The page
   */
  getLatestPaginated(page: number): Array<Review> {
    const pageSize = 4;
    return this.latestReviewList.slice(page * pageSize, (page + 1) * pageSize);
  }

  /**
   * Changes to the previous page of the given list
   * @param list A string representing the list
   */
  previous(list: string): void {
    switch (list) {
      case 'popular':
        this.popularCurrentPage--;
        break;
      default:
        this.latestCurrentPage--;
    }
  }

  /**
   * Changes to the next page of the given list
   * @param list A string representing the list
   */
  next(list: string): void {
    switch (list) {
      case 'popular':
        this.popularCurrentPage++;
        break;
      default:
        this.latestCurrentPage++;
    }
  }
}
