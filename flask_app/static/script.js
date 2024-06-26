$(document).ready(function() {
    // Smooth scroll for internal links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if(target.length) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });

    // Tab functionality
    $('.tab-link').on('click', function(event) {
        event.preventDefault();
        var tabId = $(this).data('tab');
        $('.tab-content').hide();
        $('#' + tabId).show();
    });

    // Handle search button click
    $('#search-btn').click(function() {
	var field_id = $('#fields-dropdown').val();
        var category = $('#category-dropdown').val();

        getProfiles(category);
    });

    $('#fields-dropdown').change(function() {
        var field_id = $(this).val();
        var categorySelect = $('#category-dropdown');
        categorySelect.empty();

        $.each(fieldsData, function(index, field) {
            if (field.id == field_id) {
                $.each(field.categories, function(index, category) {
                    categorySelect.append('<option value="' + category.id + '">' + category.name + '</option>');
                });
            }
        });
    }).trigger('change');


    // Update Profile form submission
    $('#update-form').on('submit', function(event) {
	event.preventDefault();
	var formData = new FormData(this);
	$.ajax({
	    type: 'POST',
	    url: '/update_profile',
	    data: formData,
	    processData: false,
	    contentType: false,
	    success: function() {
		alert('Profile updated successfully!');
		location.reload(); // Reload the page to reflect the changes
            },
            error: function(jqXHR) {
		var response = jqXHR.responseJSON;
		var message = response ? response.message : 'There was an error updating the profile.';
		alert(message);
            }
	});
    });

    // Add Skill button click event
    $('#add-skill').click(function() {
	var skillEntryHtml = `
            <div class="skill-entry">
                <input type="text" name="skills-${$('.skill-entry').length}-skill_name" placeholder="Skill" required>
                <input type="text" name="skills-${$('.skill-entry').length}-duration" placeholder="Duration (e.g., 5 years)" required>
                <button type="button" class="remove-skill">Remove</button>
             </div>
        `;
	$('#skills-container').append(skillEntryHtml);
    });

    // Remove Skill button click event
    $('#skills-container').on('click', '.remove-skill', function() {
        $(this).closest('.skill-entry').remove();
    });

    // Function to get profiles based on selected category and skill
    function getProfiles(category) {
	$.ajax({
	    type: 'GET',
	    url: '/profiles',
	    data: { category: category },
	    success: function(profiles) {
		if (profiles.length === 0) {
                    $('#profiles-container').html('<p>No profiles found. Keep searching, your perfect match might be just around the corner!</p>');
		} else {
                    displayProfiles(profiles);
		}
	    },
	    error: function() {
		alert('There was an error retrieving the profiles.');
	    }
	});
    }

    //function to populate the categories in fields dynamically
    $('#field').change(function() {
        var field_id = $(this).val();
        var categorySelect = $('#category');
        var fieldOtherInput = $('#field-other');
        categorySelect.empty();

        if (field_id == 'other') {
            fieldOtherInput.show();
            categorySelect.hide();
            $('#category-other').show();
        } else {
            fieldOtherInput.hide();
            categorySelect.show();
            $('#category-other').hide();

            $.each(fieldsData, function(index, field) {
                if (field.id == field_id) {
                    $.each(field.categories, function(index, category) {
                        categorySelect.append('<option value="' + category.id + '">' + category.name + '</option>');
                    });
                    categorySelect.append('<option value="other">Other</option>');
                }
            });
        }
    }).trigger('change');

    $('#category').change(function() {
        var category_id = $(this).val();
        if (category_id == 'other') {
            $('#category-other').show();
        } else {
            $('#category-other').hide();
        }
    });
    
    // Function to display profiles in the container
    function displayProfiles(profiles) {
        var container = $('#profiles-container');
        container.empty();
        profiles.forEach(function(profile) {
            var profileHtml = `
                <div class="profile" data-profile='${JSON.stringify(profile)}'>
                    <img src="${profile.avatar}" alt="${profile.name}">
                    <div class="profile-info">
                        <h3>${profile.name}</h3>
                        <p>${profile.description}</p>
                    </div>
                </div>
            `;
            container.append(profileHtml);
        });
	
        // Add click event to each profile to show modal
        $('.profile').on('click', function() {
            var profileData = $(this).data('profile');
            showModal(profileData);
        });
    }

    // Function to show modal with profile details
    function showModal(profile) {
        var modal = $('#profile-modal');
        var modalProfile = modal.find('.modal-profile');

        var skillsList = profile.skills.map(skill => `<li>${skill}</li>`).join('');

        var profileDetails = `
            <img src="${profile.avatar}" alt="${profile.name}">
            <h3>${profile.name}</h3>
            <p>${profile.description}</p>
            <p>Address: ${profile.address}</p>
            <p>Payment: ${profile.payment}</p>
            <p>Availability: ${profile.availability}</p>
            <div class="skills">
                <h4>Skills:</h4>
                <ul>${skillsList}</ul>
            </div>
            <p>Reviews: ${profile.reviews}</p>
            <button id="connect-btn" class="connect-btn">Connect</button>
            <div id="contact-info" style="display:none;">
                <p>Email: <a href="mailto:${profile.email}">${profile.email}</a></p>
                <p>LinkedIn: <a href="${profile.linkedin}" target="_blank">${profile.linkedin}</a></p>
                <p>GitHub: <a href="${profile.github}" target="_blank">${profile.github}</a></p>
            </div>
            <button id="collaborate-btn" class="collaborate-btn">Collaborate</button>
        `;

        modalProfile.html(profileDetails);
        modal.show();

        // Connect button click event
	$('#connect-btn').on('click', function() {
            if (logged_in) {
		$('#contact-info').toggle();
            } else {
		window.location.href = '/login';
            }
	    $(this).toggleClass('btn-default btn-success');
	});

	// Add click event for "Collaborate" button
	$('#collaborate-btn').on('click', function() {
            if (logged_in) {
		addToTeamView(profile);
		alert('Profile added to your team!');
            } else {
		window.location.href = '/login';
            }
	    $(this).toggleClass('btn-default btn-success');
	});
    }
    // Function to add profile to team view
    function addToTeamView(profile) {
        var teamContainer = $('#team-container');
        var teamHtml = `
            <div class="team-member">
                <img src="${profile.avatar}" alt="${profile.name}">
                <div class="team-info">
                    <h3>${profile.name}</h3>
                    <p>${profile.description}</p>
                </div>
            </div>
        `;
        teamContainer.append(teamHtml);
    }

    // Add click event for user avatar to log out
    $('.user-avatar').on('click', function() {
        window.location.href = '/logout';
    });

    // Close modal on click of the close button
    $('.modal .close').on('click', function() {
        $('#profile-modal').hide();
    });

    // Close modal on click outside of the modal content
    $(window).on('click', function(event) {
        if ($(event.target).is('#profile-modal')) {
            $('#profile-modal').hide();
        }
    });

    // Handle tab switching
    $('.tab-link').click(function(event) {
        event.preventDefault();
        var tabID = $(this).attr('data-tab');
        
        $('.tab-content').hide();
        $('#' + tabID).show();
        
        $('.tab-link').removeClass('active');
        $(this).addClass('active');
    });

    // Show the first tab by default
    $('.tab-link').first().click();

    // Handle modal close
    $('.close').click(function() {
        $('.modal').hide();
    });

    // Add click event for "Collaborate" button
    $('#team-view').on('click', function() {
        alert('Search skills and click collaborate to add members to your team!');
    });

    //Handling Tabs and Form Submissions
    $('.tab-link').click(function() {
        var tab_id = $(this).attr('data-tab');
        $('.tab-content').hide();
        $('#' + tab_id).show();
    });

    // Function to handle the popup logic
    function handleAuthPopup() {
        var popup = $('#auth-popup');
        var closeBtn = $('.close-btn');
        var getStartedBtn = $('#get-started-btn');
        var loginBtn = $('#login-btn');
        var signupBtn = $('#signup-btn');
        var continueBtn = $('#continue-btn');

        // Show the popup when 'Get Started' button is clicked
        getStartedBtn.on('click', function() {
            popup.show();
        });

        // Close the popup when the 'x' button is clicked
        closeBtn.on('click', function() {
            popup.hide();
        });

        // Close the popup when clicking outside of the popup content
        $(window).on('click', function(event) {
            if (event.target == popup[0]) {
                popup.hide();
            }
        });

        // Redirect to login page
        loginBtn.on('click', function() {
            window.location.href = '/login';
        });

        // Redirect to signup page
        signupBtn.on('click', function() {
            window.location.href = '/register';
        });

        // Redirect to dashboard
        continueBtn.on('click', function() {
            window.location.href = '/dashboard';
        });
    }

    // Call the function to handle the popup
    handleAuthPopup();
});
